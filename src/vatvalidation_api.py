# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import argparse
import json
import threading
import uuid
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import batch
import helper
import settings
import single

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


settings.create_config()

app = FastAPI(
    title="VATValidation REST API",
    description="REST API wrapper for VATValidation single and batch validation.",
    version=helper.VERSION,
)


class SingleValidationRequest(BaseModel):
    ownvat: str
    vat: str
    company: str
    street: str
    zip: str
    town: str
    interface: str = "vies"
    lang: str = "en"


class BatchValidationRequest(BaseModel):
    input: str
    output: str
    delimiter: str | None = None
    interface: str = "vies"
    lang: str = "en"
    ignore_validation_errors: bool = False


jobs: dict[str, dict] = {}
jobs_lock = threading.Lock()


def _configure_proxy_from_args(args):
    if args.proxy_mode is not None:
        settings.save_config("proxy_mode", args.proxy_mode)
    if args.proxy_url is not None:
        settings.save_config("proxy_url", args.proxy_url)
    if args.proxy_username is not None:
        settings.save_config("proxy_username", args.proxy_username)
    if args.proxy_password is not None:
        settings.save_config("proxy_password", args.proxy_password)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _run_batch_job(job_id: str, payload: BatchValidationRequest):
    with jobs_lock:
        jobs[job_id]["status"] = "running"
        jobs[job_id]["started_at"] = _now_iso()

    try:
        result_code = batch.validatebatch(
            inputfile=payload.input,
            outputfile=payload.output,
            lang=payload.lang,
            type=payload.interface,
            delimiter=payload.delimiter,
        )

        ok = result_code == 0 or payload.ignore_validation_errors
        with jobs_lock:
            jobs[job_id]["status"] = "finished"
            jobs[job_id]["finished_at"] = _now_iso()
            jobs[job_id]["result_code"] = result_code
            jobs[job_id]["ok"] = ok
    except Exception as e:
        logger.exception("Batch job failed")
        with jobs_lock:
            jobs[job_id]["status"] = "failed"
            jobs[job_id]["finished_at"] = _now_iso()
            jobs[job_id]["error"] = str(e)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "VATValidation API",
        "version": helper.VERSION,
        "timestamp": _now_iso(),
    }


@app.post(
    "/api/v1/validate/single",
    responses={
        422: {"description": "Invalid request"},
        500: {"description": "Internal validation error"},
    },
)
def validate_single(payload: SingleValidationRequest):
    if payload.interface not in ("bzst", "vies"):
        raise HTTPException(status_code=422, detail="interface must be either 'bzst' or 'vies'")

    try:
        result = single.validatesingle(
            key1="",
            key2="",
            ownvat=payload.ownvat,
            foreignvat=payload.vat,
            company=payload.company,
            street=payload.street,
            zip=payload.zip,
            town=payload.town,
            type=payload.interface,
            lang=payload.lang,
        )
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Single validation failed")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post(
    "/api/v1/validate/batch",
    responses={
        422: {"description": "Invalid request"},
    },
)
def validate_batch(payload: BatchValidationRequest):
    if payload.interface not in ("bzst", "vies"):
        raise HTTPException(status_code=422, detail="interface must be either 'bzst' or 'vies'")

    job_id = str(uuid.uuid4())
    with jobs_lock:
        jobs[job_id] = {
            "job_id": job_id,
            "status": "queued",
            "created_at": _now_iso(),
            "input": payload.input,
            "output": payload.output,
            "result_code": None,
            "ok": None,
            "error": None,
        }

    thread = threading.Thread(target=_run_batch_job, args=(job_id, payload), daemon=True)
    thread.start()

    return {
        "job_id": job_id,
        "status": "queued",
        "status_url": f"/api/v1/jobs/{job_id}",
    }


@app.get(
    "/api/v1/jobs/{job_id}",
    responses={
        404: {"description": "Job not found"},
    },
)
def get_job_status(job_id: str):
    with jobs_lock:
        job = jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@app.get("/api/v1/jobs")
def list_jobs():
    with jobs_lock:
        return {
            "count": len(jobs),
            "jobs": list(jobs.values()),
        }


def _parse_args():
    parser = argparse.ArgumentParser(
        description=helper.NAME + " API" + " - " + helper.VERSION,
    )
    parser.add_argument("--version", action="version", version=helper.VERSION)
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind the API server")
    parser.add_argument("--port", type=int, default=8080, help="Port to bind the API server")
    parser.add_argument(
        "--proxy-mode",
        type=str,
        choices=["system", "manual", "none"],
        required=False,
        help="Proxy mode written to config file and used by API requests.",
    )
    parser.add_argument(
        "--proxy-url",
        type=str,
        required=False,
        help="Proxy URL written to config file, e.g. http://proxy.example.com:8080",
    )
    parser.add_argument(
        "--proxy-username",
        type=str,
        required=False,
        help="Proxy username written to config file.",
    )
    parser.add_argument(
        "--proxy-password",
        type=str,
        required=False,
        help="Proxy password written to config file.",
    )
    parser.add_argument(
        "--export-openapi",
        type=str,
        required=False,
        help="Export OpenAPI specification to the given file and exit",
    )
    return parser.parse_args()


def main():
    args = _parse_args()
    _configure_proxy_from_args(args)

    if args.export_openapi:
        with open(args.export_openapi, "w", encoding="utf-8") as f:
            json.dump(app.openapi(), f, indent=2)
        print(f"OpenAPI specification exported to: {args.export_openapi}")
        return

    import uvicorn

    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
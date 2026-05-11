# REST API

VATValidation provides a FastAPI-based REST API for single and batch validation.

## Binary

The release pipeline builds dedicated API binaries:

- `VATValidation-api-windows-<version>.exe`
- `VATValidation-api-linux-<version>`

Download them from [releases](https://github.com/dseichter/VATValidation/releases).

## Start API Server

Windows:

```shell
VATValidation-api-windows-v2026-03-27.exe --host 0.0.0.0 --port 8080 --proxy-mode manual --proxy-url http://127.0.0.1:8080
```

Linux:

```shell
./VATValidation-api-linux-v2026-03-27 --host 0.0.0.0 --port 8080 --proxy-mode system
```

Default host is `0.0.0.0` and default port is `8080`.

Proxy settings are configured once at process start and written to the config file, not passed in request payload.

Logging is also configured via the same config file. Relevant keys are `logfilename` and `loglevel` (default in this repository: `/tmp/vatvalidation.log` with `ERROR`).

## Endpoints

- `GET /health`
- `POST /api/v1/validate/single`
- `POST /api/v1/validate/batch`
- `GET /api/v1/jobs/{job_id}`
- `GET /api/v1/jobs`

### Single Validation Request

```json
{
  "ownvat": "DE123456789",
  "vat": "FR12345678901",
  "company": "Sample GmbH",
  "street": "Musterstrasse 1",
  "zip": "10115",
  "town": "Berlin",
  "interface": "vies",
  "lang": "en"
}
```

### Batch Validation Request

```json
{
  "input": "input.csv",
  "output": "output.csv",
  "delimiter": ";",
  "interface": "vies",
  "lang": "en",
  "ignore_validation_errors": false
}
```

Batch validation runs asynchronously and returns a `job_id`.

## Async Batch Flow (job_id polling)

1. Start batch job:

```shell
curl -X POST http://localhost:8080/api/v1/validate/batch \
  -H "Content-Type: application/json" \
  -d '{
    "input": "input.csv",
    "output": "output.csv",
    "delimiter": ";",
    "interface": "vies",
    "lang": "en",
    "ignore_validation_errors": false
  }'
```

Example response:

```json
{
  "job_id": "d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8",
  "status": "queued",
  "status_url": "/api/v1/jobs/d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8"
}
```

2. Query current state by `job_id`:

```shell
curl http://localhost:8080/api/v1/jobs/d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8
```

Example response while running:

```json
{
  "job_id": "d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8",
  "status": "running",
  "created_at": "2026-05-11T10:00:00+00:00",
  "started_at": "2026-05-11T10:00:01+00:00",
  "input": "input.csv",
  "output": "output.csv",
  "result_code": null,
  "ok": null,
  "error": null
}
```

Example response when finished:

```json
{
  "job_id": "d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8",
  "status": "finished",
  "created_at": "2026-05-11T10:00:00+00:00",
  "started_at": "2026-05-11T10:00:01+00:00",
  "finished_at": "2026-05-11T10:00:08+00:00",
  "input": "input.csv",
  "output": "output.csv",
  "result_code": 0,
  "ok": true,
  "error": null
}
```

3. Optional: list all current jobs stored in memory:

```shell
curl http://localhost:8080/api/v1/jobs
```

## OpenAPI Specification

FastAPI automatically serves:

- OpenAPI JSON: `GET /openapi.json`
- Swagger UI: `GET /docs`
- ReDoc: `GET /redoc`

Additionally, a static reference specification is available in this repository at `docs/docs/openapi.yaml`.

You can also export the OpenAPI specification from the binary:

Windows:

```shell
VATValidation-api-windows-v2026-03-27.exe --export-openapi openapi.json
```

Linux:

```shell
./VATValidation-api-linux-v2026-03-27 --export-openapi openapi.json
```
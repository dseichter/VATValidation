# REST API

VATValidation bietet eine FastAPI-basierte REST-API für Einzel- und Batch-Validierung.

## Binärdatei

Die Release-Pipeline erstellt eigene API-Binaries:

- `VATValidation-api-windows-<version>.exe`
- `VATValidation-api-linux-<version>`

Download über [Releases](https://github.com/dseichter/VATValidation/releases).

## API-Server starten

Windows:

```shell
VATValidation-api-windows-v2026-05-12.exe --host 0.0.0.0 --port 8080 --proxy-mode manual --proxy-url http://127.0.0.1:8080
```

Linux:

```shell
./VATValidation-api-linux-v2026-05-12 --host 0.0.0.0 --port 8080 --proxy-mode system
```

Standard ist `0.0.0.0` als Host und `8080` als Port.

Proxy-Einstellungen werden einmal beim Start gesetzt und in die Konfigurationsdatei geschrieben, nicht im Request-Payload übergeben.

Das Logging wird ebenfalls über diese Konfigurationsdatei gesteuert. Relevante Schlüssel sind `logfilename` und `loglevel` (Standard in diesem Repository: `/tmp/vatvalidation.log` mit `ERROR`).

## Endpunkte

- `GET /health`
- `POST /api/v1/validate/single`
- `POST /api/v1/validate/batch`
- `GET /api/v1/jobs/{job_id}`
- `GET /api/v1/jobs`

### Request für Einzelvalidierung

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

### Request für Batch-Validierung

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

Die Batch-Validierung läuft asynchron und liefert eine `job_id` zurück.

## Asynchroner Batch-Ablauf (job_id Polling)

1. Batch-Job starten:

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

Beispielantwort:

```json
{
  "job_id": "d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8",
  "status": "queued",
  "status_url": "/api/v1/jobs/d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8"
}
```

2. Aktuellen Status über `job_id` abfragen:

```shell
curl http://localhost:8080/api/v1/jobs/d5242f38-6e3a-4f75-9d0e-3d8cc9f4e5a8
```

Beispielantwort während der Verarbeitung:

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

Beispielantwort nach Abschluss:

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

3. Optional: alle aktuell im Speicher gehaltenen Jobs auflisten:

```shell
curl http://localhost:8080/api/v1/jobs
```

## OpenAPI-Spezifikation

FastAPI stellt automatisch bereit:

- OpenAPI JSON: `GET /openapi.json`
- Swagger UI: `GET /docs`
- ReDoc: `GET /redoc`

Zusätzlich gibt es eine statische Referenz-Spezifikation in diesem Repository unter `docs/docs/openapi.yaml`.

Sie können die OpenAPI-Spezifikation auch aus der Binärdatei exportieren:

Windows:

```shell
VATValidation-api-windows-v2026-05-12.exe --export-openapi openapi.json
```

Linux:

```shell
./VATValidation-api-linux-v2026-05-12 --export-openapi openapi.json
```
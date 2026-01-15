# Dateiformate und Felder

VATValidation unterstützt die Batch-Verarbeitung in den Dateiformaten **CSV**, **JSON** und **XLSX**. Diese Seite beschreibt die erforderlichen Eingabefelder und erwarteten Ausgabefelder für jedes Format.

## Eingabefelder

Wenn Sie eine Batch-Datei zur Validierung erstellen, müssen Sie die folgenden 8 Spalten/Felder enthalten:

| Feldname | Beschreibung | Erforderlich | Beispiel |
|----------|-------------|--------------|----------|
| `key1` | Erster Teil Ihrer eigenen Steuernummer (Ländercode) | Ja | `DE` |
| `key2` | Zweiter Teil Ihrer eigenen Steuernummer (Steuernummer) | Ja | `123456789` |
| `ownvat` | Ihre vollständige Steuernummer | Ja | `DE123456789` |
| `foreignvat` | Die ausländische Steuernummer zur Validierung | Ja | `FR12345678901` |
| `company` | Unternehmensname (optional zur Validierung, aber erforderlich als Feld) | Nein | `Acme GmbH` |
| `street` | Straßenadresse (optional zur Validierung, aber erforderlich als Feld) | Nein | `Hauptstraße 42` |
| `zip` | Postleitzahl (optional zur Validierung, aber erforderlich als Feld) | Nein | `12345` |
| `town` | Stadt/Ort (optional zur Validierung, aber erforderlich als Feld) | Nein | `Berlin` |

### Beispiele für Eingabedaten

#### CSV-Format

Das Trennzeichen kann konfiguriert werden.

```csv
key1,key2,ownvat,foreignvat,company,street,zip,town
DE,123456789,DE123456789,FR40303265045,Beispiel GmbH,Hauptstr. 42,10115,Berlin
DE,123456789,DE123456789,IT12345678901,Test Unternehmen,Berliner Str. 10,20095,München
```

#### JSON-Format

```json
[
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "FR40303265045",
    "company": "Beispiel GmbH",
    "street": "Hauptstr. 42",
    "zip": "10115",
    "town": "Berlin"
    },
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "IT12345678901",
    "company": "Test Unternehmen",
    "street": "Berliner Str. 10",
    "zip": "20095",
    "town": "München"
    }
]
```

#### XLSX-Format

```xlsx
| key1 | key2 | ownvat | foreignvat | company | street | zip | town |
|------|------|--------|-----------|---------|--------|-----|------|
| DE | 123456789 | DE123456789 | FR40303265045 | Beispiel GmbH | Hauptstr. 42 | 10115 | Berlin |
| DE | 123456789 | DE123456789 | IT12345678901 | Test Unternehmen | Berliner Str. 10 | 20095 | München |
```

## Ausgabefelder

Nach der Validierung enthält die Ausgabedatei die Validierungsergebnisse mit den folgenden Feldern:

| Feldname | Beschreibung |
|----------|-------------|
| `key1` | Erster Teil Ihrer eigenen Steuernummer (Ländercode) |
| `key2` | Zweiter Teil Ihrer eigenen Steuernummer (Steuernummer) |
| `ownvat` | Ihre vollständige Steuernummer |
| `foreignvat` | Die ausländische Steuernummer, die validiert wurde |
| `type` | Validierungsquelle ("vies" oder "hmrc") |
| `valid` | Gibt an, ob die Steuernummer gültig ist (wahr/falsch) |
| `errorcode` | Fehlercode bei fehlgeschlagener Validierung |
| `errorcode_description` | Lesbare Beschreibung des Fehlercodes |
| `valid_from` | Datum, ab dem die Steuernummer gültig ist (falls verfügbar) |
| `valid_to` | Datum, bis zu dem die Steuernummer gültig ist (falls verfügbar) |
| `timestamp` | ISO-Format-Datum der Validierungsprüfung |
| `company` | Mit der Steuernummer verbundener Unternehmensname |
| `address` | Mit der Steuernummer verbundene Adresse |
| `town` | Stadt/Ort (aus der Adresse extrahiert, falls verfügbar) |
| `zip` | Postleitzahl (aus der Adresse extrahiert, falls verfügbar) |
| `street` | Straßenadresse (aus der Adresse extrahiert, falls verfügbar) |

### Beispiele für Ausgabedaten

#### CSV-Format

```csv
key1,key2,ownvat,foreignvat,type,valid,errorcode,errorcode_description,valid_from,valid_to,timestamp,company,address,town,zip,street
DE,123456789,DE123456789,FR40303265045,vies,true,,Gültige Steuernummer,,,2025-01-15T10:30:00,Beispiel AG,"Beispiel AG, Hauptstr. 10, 75001 Paris",Paris,75001,Hauptstr. 10
DE,123456789,DE123456789,IT12345678901,vies,false,INVALID,,,,2025-01-15T10:30:01,,,,,
```

#### JSON-Format

```json
[
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "FR40303265045",
    "type": "vies",
    "valid": true,
    "errorcode": "",
    "errorcode_description": "Gültige Steuernummer",
    "valid_from": "",
    "valid_to": "",
    "timestamp": "2025-01-15T10:30:00",
    "company": "Beispiel AG",
    "address": "Beispiel AG, Hauptstr. 10, 75001 Paris",
    "town": "Paris",
    "zip": "75001",
    "street": "Hauptstr. 10"
    },
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "IT12345678901",
    "type": "vies",
    "valid": false,
    "errorcode": "INVALID",
    "errorcode_description": "Ungültige Steuernummer",
    "valid_from": "",
    "valid_to": "",
    "timestamp": "2025-01-15T10:30:01",
    "company": "",
    "address": "",
    "town": "",
    "zip": "",
    "street": ""
    }
]
```

#### XLSX-Format

```xlsx
| key1 | key2 | ownvat | foreignvat | type | valid | errorcode | errorcode_description | valid_from | valid_to | timestamp | company | address | town | zip | street |
|------|------|--------|-----------|------|-------|-----------|----------------------|------------|----------|-----------|---------|---------|------|-----|--------|
| DE | 123456789 | DE123456789 | FR40303265045 | vies | TRUE | | Gültige Steuernummer | | | 2025-01-15T10:30:00 | Beispiel AG | Beispiel AG, Hauptstr. 10, 75001 Paris | Paris | 75001 | Hauptstr. 10 |
| DE | 123456789 | DE123456789 | IT12345678901 | vies | FALSE | INVALID | Ungültige Steuernummer | | | 2025-01-15T10:30:01 | | | | | |
```

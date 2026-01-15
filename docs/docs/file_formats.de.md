# Dateiformate und Felder

VATValidation unterstützt die Batch-Verarbeitung in den Dateiformaten **CSV**, **JSON** und **XLSX**. Diese Seite beschreibt die erforderlichen Eingabefelder und erwarteten Ausgabefelder für jedes Format.

## Eingabefelder

Wenn Sie eine Batch-Datei zur Validierung erstellen, müssen Sie die folgenden 8 Spalten/Felder in dieser exakten Reihenfolge enthalten:

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

=== "CSV-Format"

    ```csv
    key1,key2,ownvat,foreignvat,company,street,zip,town
    DE,123456789,DE123456789,FR40303265045,Beispiel GmbH,Hauptstr. 42,10115,Berlin
    DE,123456789,DE123456789,IT12345678901,Test Unternehmen,Berliner Str. 10,20095,München
    ```

=== "JSON-Format"

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

=== "XLSX-Format"

    | key1 | key2 | ownvat | foreignvat | company | street | zip | town |
    |------|------|--------|-----------|---------|--------|-----|------|
    | DE | 123456789 | DE123456789 | FR40303265045 | Beispiel GmbH | Hauptstr. 42 | 10115 | Berlin |
    | DE | 123456789 | DE123456789 | IT12345678901 | Test Unternehmen | Berliner Str. 10 | 20095 | München |

## Ausgabefelder

Nach der Validierung enthält die Ausgabedatei die Validierungsergebnisse mit den folgenden Feldern:

| Feldname | Typ | Beschreibung |
|----------|-----|-------------|
| `statusCode` | Ganzzahl | HTTP-ähnlicher Statuscode, der das Validierungsergebnis anzeigt (z.B. 200 für Erfolg, 406 für Fehler) |
| `body` | Zeichenkette (JSON) | Enthält die detaillierte Validierungsantwort als JSON-Zeichenkette |

Das `body`-Feld enthält ein JSON-Objekt mit der folgenden Struktur:

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `errorcode` | Zeichenkette | Fehlercode bei fehlgeschlagener Validierung (z.B. "VAT0001" für fehlende Felder) |
| `message` | Zeichenkette | Aussagekräftige Nachricht über das Validierungsergebnis oder einen Fehler |
| `valid` | Wahrheitswert | Gibt an, ob die Steuernummer gültig ist |
| `address` | Zeichenkette | Die mit der Steuernummer verbundene Adresse (falls verfügbar) |
| `name` | Zeichenkette | Der mit der Steuernummer verbundene Unternehmensname (falls verfügbar) |
| `requestIdentifier` | Zeichenkette | Eindeutige Request-ID vom Validierungsdienst |
| `consumerAddress` | Zeichenkette | Adresse des Verbrauchers/Antragstellers (für VIES-Validierung) |
| `consumerName` | Zeichenkette | Name des Verbrauchers/Antragstellers (für VIES-Validierung) |
| `checkDate` | Zeichenkette | ISO-Format-Datum der Validierungsprüfung |

### Beispiele für Ausgabedaten

=== "CSV-Format"

    ```csv
    statusCode,body
    200,"{""valid"": true, ""address"": ""Beispiel AG, Hauptstr. 10, 75001 Paris"", ""name"": ""Beispiel AG"", ""message"": ""Die Steuernummer ist gültig.""}"
    200,"{""valid"": false, ""message"": ""Die Steuernummer ist nicht gültig.""}"
    406,"{""errorcode"": ""VAT0001"", ""message"": ""Das folgende Feld fehlt: foreignvat""}"
    ```

=== "JSON-Format"

    ```json
    [
      {
        "statusCode": 200,
        "body": "{\"valid\": true, \"address\": \"Beispiel AG, Hauptstr. 10, 75001 Paris\", \"name\": \"Beispiel AG\", \"message\": \"Die Steuernummer ist gültig.\"}"
      },
      {
        "statusCode": 200,
        "body": "{\"valid\": false, \"message\": \"Die Steuernummer ist nicht gültig.\"}"
      },
      {
        "statusCode": 406,
        "body": "{\"errorcode\": \"VAT0001\", \"message\": \"Das folgende Feld fehlt: foreignvat\"}"
      }
    ]
    ```

=== "XLSX-Format"

    | statusCode | body |
    |------------|------|
    | 200 | {"valid": true, "address": "Beispiel AG, Hauptstr. 10, 75001 Paris", "name": "Beispiel AG"} |
    | 200 | {"valid": false, "message": "Die Steuernummer ist nicht gültig."} |
    | 406 | {"errorcode": "VAT0001", "message": "Das folgende Feld fehlt: foreignvat"} |

## Dateikonfiguration

### CSV-Trennzeichen

Sie können das Trennzeichen für CSV-Dateien über den **Konfiguration**-Tab in der GUI konfigurieren. Häufig verwendete Trennzeichen sind:

- `,` (Komma) - Standard
- `;` (Semikolon)
- `\t` (Tabulator)

Die gleiche Trennzeicheneinstellung gilt für Ein- und Ausgabe-CSV-Dateien.

## Hinweise zur Verwendung

1. **Alle Eingabefelder sind erforderlich** - Auch wenn einige (wie company, street, zip, town) optional für die Validierung sind, müssen sie in der Datei vorhanden sein.

2. **Spaltenreihenfolge** - Die Eingabespalten müssen in der exakt angegebenen Reihenfolge vorliegen (key1, key2, ownvat, foreignvat, company, street, zip, town).

3. **Steuernummernformat** - Das `foreignvat`-Feld sollte die vollständige Steuernummer einschließlich des Ländercodes enthalten (z.B. `FR40303265045` für Frankreich).

4. **Ausgabedatei** - Standardmäßig verwendet die Ausgabedatei das gleiche Format und Trennzeichen wie die Eingabedatei. Wenn Sie keine Ausgabedatei angeben, wird eine mit dem gleichen Namen wie die Eingabedatei erstellt, aber mit `.log.` vor der Erweiterung (z.B. `input.csv` → `input.log.csv`).

5. **JSON-Body-Feld** - Beachten Sie, dass die detaillierten Ergebnisse in der Ausgabe als JSON-Zeichenkette im `body`-Feld gespeichert sind. Möglicherweise müssen Sie diese Zeichenkette analysieren, um auf einzelne Ergebnisfelder zuzugreifen.

6. **Validierungs-API** - Je nach Ihrer Konfiguration kann die Validierung entweder:
   - **VIES** - für EU-Steuernummern
   - **HMRC** - für britische Steuernummern

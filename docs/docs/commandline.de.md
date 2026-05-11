# Kommandozeilen-Tool

Das CLI-Tool unterstützt zwei Modi: **Stapelverarbeitung** zum Validieren von Listen mit Umsatzsteuer-IDs aus Dateien und **Einzelvalidierung** zum Validieren einzelner Umsatzsteuer-IDs.

## Download

Um das CLI-Tool zu verwenden, laden Sie die neueste Version herunter, wie z.B. `VATValidation-cli-windows-...exe` und benennen Sie es in `vatvalidation_cli.exe` um.

## Verwendung

Führen Sie das Tool aus, um die verfügbaren Optionen anzuzeigen:

```shell
vatvalidation_cli.exe
```

Validieren Sie mehrere Umsatzsteuer-IDs aus einer Datei (CSV, XLSX oder JSON):

```shell
usage: vatvalidation_cli.py [-h] [--version] [--input INPUT] [--output OUTPUT]
                            [--delimiter DELIMITER] [--interface INTERFACE]
                            [--proxy-mode {system,manual,none}] [--proxy-url PROXY_URL]
                            [--proxy-username PROXY_USERNAME] [--proxy-password PROXY_PASSWORD]
                            [--ignore-validation-errors]

VATValidation CLI - v2026-02-03

Modi:
  Batch-Modus: Verwenden Sie --input und --output zur Validierung einer Liste von Umsatzsteuer-IDs aus einer Datei
  Einzelmodus: Verwenden Sie --ownvat, --vat, --company, --street, --zip, --town für Einzelvalidierung

Optionen:
  -h, --help            Hilfe anzeigen und beenden
  --version             Version anzeigen und beenden
  --input INPUT         Eingabedatei für Umsatzsteuer-IDs (Batch-Modus)
  --output OUTPUT       Ausgabedatei für Validierungsergebnisse (Batch-Modus)
  --delimiter DELIM     Optionales CSV-Trennzeichen (einzelnes Zeichen). Beispiele: 
                        `--delimiter ,` oder `--delimiter ';'` oder `--delimiter "\\t"`
  --ownvat OWNVAT       Ihre Umsatzsteuer-ID (Einzelmodus)
  --vat VAT             Umsatzsteuer-ID zur Validierung (Einzelmodus)
  --company COMPANY     Firmenname (Einzelmodus)
  --street STREET       Straßenadresse (Einzelmodus)
  --zip ZIP             Postleitzahl (Einzelmodus)
  --town TOWN           Stadt/Ort (Einzelmodus)
  --interface INTERFACE Schnittstelle für die Validierung überschreiben. 
                        Zulässige Werte sind: bzst,vies
  --proxy-mode {system,manual,none}
                        Proxy-Modus für Netzwerkanfragen
  --proxy-url PROXY_URL Manuelle Proxy-URL, z.B. http://proxy.example.com:8080
  --proxy-username PROXY_USERNAME
                        Benutzername für Proxy-Authentifizierung
  --proxy-password PROXY_PASSWORD
                        Passwort für Proxy-Authentifizierung
  --ignore-validation-errors
                        Geben Sie Exit-Code 0 zurück, auch wenn die Validierung fehlschlägt. 
                        Nützlich für die Integration in andere Anwendungen
```

## Beispiele

### Beispiel für Stapelverarbeitung

Unter Windows:

```shell
vatvalidation_cli.exe --input input.csv --output results.csv
```

Unter Linux/macOS:

```shell
./vatvalidation_cli --input input.csv --output results.csv
```

Mit benutzerdefiniertem Trennzeichen und Schnittstelle:

```shell
vatvalidation_cli.exe --input input.csv --output results.csv --delimiter ";" --interface bzst
```

### Beispiel für Einzelvalidierung

Validieren Sie eine einzelne Umsatzsteuer-ID:

```shell
vatvalidation_cli.exe --ownvat "DE123456789" --vat "FR12345678901" --company "ACME Corporation" --street "Hauptstraße 123" --zip "75001" --town "Paris"
```

Mit benutzerdefinierter Schnittstelle:

```shell
vatvalidation_cli.exe --ownvat "DE123456789" --vat "DE987654321" --company "Test GmbH" --street "Hauptstraße 42" --zip "10115" --town "Berlin" --interface bzst
```

### Integration mit deaktivierter Fehlerbehandlung

Für die Integration in Anwendungen, bei denen Validierungsfehler den Prozess nicht unterbrechen sollten:

```shell
vatvalidation_cli.exe --input input.csv --output results.csv --ignore-validation-errors
```

Oder für Einzelvalidierung:

```shell
vatvalidation_cli.exe --ownvat "DE123456789" --vat "FR12345678901" --company "ACME Corp" --street "Hauptstraße 123" --zip "75001" --town "Paris" --ignore-validation-errors
```

## Proxy-Konfiguration

### Beispiel für manuellen Proxy

```shell
vatvalidation_cli.exe --input input.csv --output output.csv --proxy-mode manual --proxy-url http://127.0.0.1:8080
```

Mit Proxy-Authentifizierung:

```shell
vatvalidation_cli.exe --input input.csv --output output.csv --proxy-mode manual --proxy-url http://127.0.0.1:8080 --proxy-username user --proxy-password pass
```

### Beispiel für System-Proxy

Unter Windows:

```shell
set HTTP_PROXY=http://127.0.0.1:8080
set HTTPS_PROXY=http://127.0.0.1:8080
vatvalidation_cli.exe --input input.csv --output output.csv --proxy-mode system
```

Unter Linux/macOS:

```shell
export HTTP_PROXY=http://127.0.0.1:8080
export HTTPS_PROXY=http://127.0.0.1:8080
./vatvalidation_cli --input input.csv --output output.csv --proxy-mode system
```
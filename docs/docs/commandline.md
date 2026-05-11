# Command Line tool

The CLI tool supports two modes: **batch processing** for validating lists of VAT numbers from files, and **single validation** for validating individual VAT numbers.

## Download

To use the CLI tool, download the latest release like `VATValidation-cli-windows-...exe` and rename it to `vatvalidation_cli.exe`.

## Usage

Run the tool to see available options:

```shell
vatvalidation_cli.exe
```

Validate multiple VAT numbers from a file (CSV, XLSX, or JSON):

```shell
usage: vatvalidation_cli.py [-h] [--version] [--input INPUT] [--output OUTPUT]
                            [--delimiter DELIMITER] [--interface INTERFACE]
                            [--proxy-mode {system,manual,none}] [--proxy-url PROXY_URL]
                            [--proxy-username PROXY_USERNAME] [--proxy-password PROXY_PASSWORD]
                            [--ignore-validation-errors]

VATValidation CLI - v2026-02-03

Modes:
  Batch mode: Use --input and --output to validate a list of VAT numbers from a file
  Single mode: Use --ownvat, --vat, --company, --street, --zip, --town for single validation

options:
  -h, --help            show this help message and exit
  --version             show version and exit
  --input INPUT         Input filename for VAT numbers (batch mode)
  --output OUTPUT       Output filename for validation results (batch mode)
  --delimiter DELIM     Optional CSV delimiter (single character). For example: 
                        `--delimiter ,` or `--delimiter ';'` or `--delimiter "\\t"`
  --ownvat OWNVAT       Own VAT number (single mode)
  --vat VAT             VAT number to validate (single mode)
  --company COMPANY     Company name (single mode)
  --street STREET       Street address (single mode)
  --zip ZIP             ZIP/postal code (single mode)
  --town TOWN           Town/city (single mode)
  --interface INTERFACE Overwrite the interface to be used during validation. 
                        Accepted values are: bzst,vies
  --proxy-mode {system,manual,none}
                        Proxy mode for network requests
  --proxy-url PROXY_URL Manual proxy URL, e.g. http://proxy.example.com:8080
  --proxy-username PROXY_USERNAME
                        Username for manual proxy authentication
  --proxy-password PROXY_PASSWORD
                        Password for manual proxy authentication
  --ignore-validation-errors
                        Return exit code 0 even if validation fails. Useful for 
                        integration into other applications
```

## Examples

### Batch Processing Example

```shell
vatvalidation_cli.exe --input input.csv --output results.csv
```

On Linux/macOS:

```shell
./vatvalidation_cli --input input.csv --output results.csv
```

With custom delimiter and interface:

```shell
vatvalidation_cli.exe --input input.csv --output results.csv --delimiter ";" --interface bzst
```

### Single Validation Example

Validate a single VAT number:

```shell
vatvalidation_cli.exe --ownvat "DE123456789" --vat "FR12345678901" --company "ACME Corporation" --street "123 Main Street" --zip "75001" --town "Paris"
```

With custom interface:

```shell
vatvalidation_cli.exe --ownvat "DE123456789" --vat "DE987654321" --company "Test GmbH" --street "Hauptstraße 42" --zip "10115" --town "Berlin" --interface bzst
```

### Integration with Error Handling Disabled

For application integration where validation failures should not terminate the process:

```shell
vatvalidation_cli.exe --input input.csv --output results.csv --ignore-validation-errors
```

Or for single validation:

```shell
vatvalidation_cli.exe --ownvat "DE123456789" --vat "FR12345678901" --company "ACME Corp" --street "123 Main Street" --zip "75001" --town "Paris" --ignore-validation-errors
```

## Proxy Configuration

### Manual Proxy Example

```shell
vatvalidation_cli.exe --input input.csv --output output.csv --proxy-mode manual --proxy-url http://127.0.0.1:8080
```

With proxy authentication:

```shell
vatvalidation_cli.exe --input input.csv --output output.csv --proxy-mode manual --proxy-url http://127.0.0.1:8080 --proxy-username user --proxy-password pass
```

### System Proxy Example

On Windows:

```shell
set HTTP_PROXY=http://127.0.0.1:8080
set HTTPS_PROXY=http://127.0.0.1:8080
vatvalidation_cli.exe --input input.csv --output output.csv --proxy-mode system
```

On Linux/macOS:

```shell
export HTTP_PROXY=http://127.0.0.1:8080
export HTTPS_PROXY=http://127.0.0.1:8080
./vatvalidation_cli --input input.csv --output output.csv --proxy-mode system
```

## REST API Proxy Note

For the REST API binary, proxy settings are configured at process start and written to the config file, not passed in API payload.

Example:

```shell
VATValidation-api-windows-v2026-03-27.exe --host 0.0.0.0 --port 8080 --proxy-mode manual --proxy-url http://127.0.0.1:8080
```

See [REST API](api.md) for details.

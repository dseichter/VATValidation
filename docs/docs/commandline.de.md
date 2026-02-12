# Kommandozeilen-Tool

Wenn Sie Batch-Dateien (z.B. json, csv oder XLSX) prüfen möchten, können Sie die neuste Versionen bspw. `VATValidation-cli-windows-...exe` herunterladen und in vatvalidation_cli.exe umbenennen.

Führen Sie das Tool einfach aus, indem Sie eine Eingabe- und eine Ausgabedatei angeben. Für weitere Informationen, führen Sie bitte folgenden Befehl aus:

``vatvalidation_cli.exe``

```shell
usage: vatvalidation_cli.py [-h] [--version] --input INPUT --output OUTPUT

VATValidation CLI - v2026-02-03

options:
  -h, --help       show this help message and exit
  --version        show version of and exit
  --input INPUT    Input filename for VAT numbers.
  --output OUTPUT  Output filename for validation results.

Additional options
  --delimiter DELIM  Optional CSV delimiter (single character) to use for this import. For
                      example: `--delimiter ,` or `--delimiter ';'` or `--delimiter "\\t"`.
  --interface INTERFACE
                        Overwrite the interface to be used during validation. Accepted values are: bzst,vies                  

For more information, visit our GitHub repository: https://github.com/dseichter/VATValidation License: GPL 3.0 - see LICENSE file at the root of the repository for details.
```

Es wird nur die Stapelverarbeitung im Moment angeboten.
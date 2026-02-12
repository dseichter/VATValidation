# Command Line tool

If you want to check batch files (e.g. json, csv or XLSX) you can download the latest releases like `VATValidation-cli-windows-...exe` and rename it to vatvalidation_cli.exe.

Just run the tool and by providing an input and an output file. For further information, please run

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

Only batch processing is currently provided.

# Configuration

The configuration is done really simple. Change to the configuration tab and enter your own vat. This will be used for the single validation as default VAT. 
Next to this, you can choose your default interface. Change the language of your output.

![configuration](assets/config.png "VATValidation Configuration")

In case you are using CSV, you can choose the delimiter for your import and export files.

## Configuration File Keys

The configuration is stored in `config.json` with the following keys:

| Key | Type | Description | Example |
|-----|------|-------------|---------|
| `delimiter` | string | Delimiter used for CSV import/export | `"|"` |
| `interface` | string | Default validation interface to use | `"vies"` |
| `language` | string | User interface language | `"en"` |
| `logfilename` | string | Path to the log file | `"/tmp/vatvalidation.log"` |
| `loglevel` | string | Log level (DEBUG, INFO, WARNING, ERROR) | `"ERROR"` |
| `theme` | string | Application theme (system, light, dark) | `"system"` |

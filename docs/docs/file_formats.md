# File Formats and Fields

VATValidation supports batch processing with **CSV**, **JSON**, and **XLSX** file formats. This page describes the required input fields and expected output fields for each format.

## Input Fields

When creating a batch file for validation, you must include the following 8 columns/fields:

| Field Name | Description | Required | Example |
|------------|-------------|----------|---------|
| `key1` | First part of your own VAT number (country code) | Yes | `DE` |
| `key2` | Second part of your own VAT number (VAT ID) | Yes | `123456789` |
| `ownvat` | Your complete VAT number | Yes | `DE123456789` |
| `foreignvat` | The foreign VAT number to validate | Yes | `FR12345678901` |
| `company` | Company name (optional for validation, but required as field) | No | `Acme Corp` |
| `street` | Street address (optional for validation, but required as field) | No | `Main Street 42` |
| `zip` | ZIP/Postal code (optional for validation, but required as field) | No | `12345` |
| `town` | City/Town name (optional for validation, but required as field) | No | `Berlin` |

### Example Input Data

#### CSV Format

The delimiter can be configured.

```csv
key1,key2,ownvat,foreignvat,company,street,zip,town
DE,123456789,DE123456789,FR40303265045,Example GmbH,Main St 42,10115,Berlin
DE,123456789,DE123456789,IT12345678901,Test Company,Berlin Str 10,20095,Munich
```

Please use always UTF-8 as encoding, to be sure, all characters are imported correct.

#### JSON Format

```json
[
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "FR40303265045",
    "company": "Example GmbH",
    "street": "Main St 42",
    "zip": "10115",
    "town": "Berlin"
    },
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "IT12345678901",
    "company": "Test Company",
    "street": "Berlin Str 10",
    "zip": "20095",
    "town": "Munich"
    }
]
```

#### XLSX Format

```xlsx
| key1 | key2 | ownvat | foreignvat | company | street | zip | town |
|------|------|--------|-----------|---------|--------|-----|------|
| DE | 123456789 | DE123456789 | FR40303265045 | Example GmbH | Main St 42 | 10115 | Berlin |
| DE | 123456789 | DE123456789 | IT12345678901 | Test Company | Berlin Str 10 | 20095 | Munich |
```

## Output Fields

After validation, the output file will contain the validation results with the following fields:

| Field Name | Description |
|------------|-------------|
| `key1` | First part of your own VAT number (country code) |
| `key2` | Second part of your own VAT number (VAT ID) |
| `ownvat` | Your complete VAT number |
| `foreignvat` | The foreign VAT number that was validated |
| `type` | Validation source ("vies" or "hmrc") |
| `valid` | Whether the VAT number is valid (true/false) |
| `errorcode` | Error code if validation failed |
| `errorcode_description` | Human-readable description of the error code |
| `valid_from` | Date from which the VAT number is valid (if available) |
| `valid_to` | Date until which the VAT number is valid (if available) |
| `timestamp` | ISO format date of the validation check |
| `company` | Company name associated with the VAT number |
| `address` | Address associated with the VAT number |
| `town` | City/Town name (extracted from address if available) |
| `zip` | ZIP/Postal code (extracted from address if available) |
| `street` | Street address (extracted from address if available) |

### Example Output Data

#### CSV Format

```csv
key1,key2,ownvat,foreignvat,type,valid,errorcode,errorcode_description,valid_from,valid_to,timestamp,company,address,town,zip,street
DE,123456789,DE123456789,FR40303265045,vies,true,,Valid VAT number,,,2025-01-15T10:30:00,Example Corp,"Example Corp, Main St 10, 75001 Paris",Paris,75001,Main St 10
DE,123456789,DE123456789,IT12345678901,vies,false,INVALID,,,,2025-01-15T10:30:01,,,,,
```

#### JSON Format

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
    "errorcode_description": "Valid VAT number",
    "valid_from": "",
    "valid_to": "",
    "timestamp": "2025-01-15T10:30:00",
    "company": "Example Corp",
    "address": "Example Corp, Main St 10, 75001 Paris",
    "town": "Paris",
    "zip": "75001",
    "street": "Main St 10"
    },
    {
    "key1": "DE",
    "key2": "123456789",
    "ownvat": "DE123456789",
    "foreignvat": "IT12345678901",
    "type": "vies",
    "valid": false,
    "errorcode": "INVALID",
    "errorcode_description": "Invalid VAT number",
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

#### XLSX Format

```xlsx
| key1 | key2 | ownvat | foreignvat | type | valid | errorcode | errorcode_description | valid_from | valid_to | timestamp | company | address | town | zip | street |
|------|------|--------|-----------|------|-------|-----------|----------------------|------------|----------|-----------|---------|---------|------|-----|--------|
| DE | 123456789 | DE123456789 | FR40303265045 | vies | TRUE | | Valid VAT number | | | 2025-01-15T10:30:00 | Example Corp | Example Corp, Main St 10, 75001 Paris | Paris | 75001 | Main St 10 |
| DE | 123456789 | DE123456789 | IT12345678901 | vies | FALSE | INVALID | Invalid VAT number | | | 2025-01-15T10:30:01 | | | | | |
```
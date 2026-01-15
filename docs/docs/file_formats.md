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

```csv
key1,key2,ownvat,foreignvat,company,street,zip,town
DE,123456789,DE123456789,FR40303265045,Example GmbH,Main St 42,10115,Berlin
DE,123456789,DE123456789,IT12345678901,Test Company,Berlin Str 10,20095,Munich
```

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
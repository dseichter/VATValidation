# VATValidation

Validate VAT number using the interfaces of BZSt, VIES and/or HMRC. Provides single or batch validation with support for CSV, XLSX and JSON.

This is the successor of my VAT-Validation, released as commercial software. After closing my company I proceeded with the migration to Python.

## Badges

![pep8](https://github.com/dseichter/VATValidation/actions/workflows/pep8.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)

## About

VAT Validation supports you in checking and validating your master data. Whether you want to check a VAT number directly at your workplace or integrate it into your ERP/CRM applications.

### Single Validation

You can use the software at your workplace and check directly against the official supported interfaces of BZSt, VIES and/or HMRC.

![single validation](images/single.png "VAT Validation Single Validtion")

### Batch Validation

Export your master data into a file (JSON, XLSX or CSV) format and check them completly.

![batch validation](images/batch.png "VAT Validation Batch Processing")

## Configuration

The configuration is done really simple. Change to the configuration tab and enter your own vat. This will be used for the single validation as default VAT. 
Next to this, you can choose your default interface. If you own a german VAT, it is recommended to use BZSt. Change the language of your output.

![configuration](images/config.png "VAT Validation Configuration")

In case you are using CSV, you can choose the delimiter for your import and export files.

# Contributing

If you want to contribute by fixing an issue, add a new function or just optimize something, a simple instruction how to start development.

## Start development

Create and activate an environment by running the following command:

```python -m venv .venv```

```.venv/Scripts/activate```

Install the required dependencies

```pip install -r src/requirements.txt```

If you want to do some UI changes, download and install the latest wxFormBuilder from the [wxFormBuilder Homepage](https://github.com/wxFormBuilder/wxFormBuilder).

You can start the VATValidation by running the following command:

```python src/vatvalidation.py```

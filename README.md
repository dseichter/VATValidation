# VATValidation

User interface for the [VATValidation](https://github.com/dseichter/VATValidation) written in Python and wx. Use single or batch validation with support for CSV, XLSX and JSON.

## Badges

![pep8](https://github.com/dseichter/VATValidation/actions/workflows/pep8.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)

## Start development

Create and activate an environment by running the following command:

```python -m venv .venv```

```.venv/Scripts/activate```

Install the required dependencies

```pip install -r src/requirements.txt```

If you want to do some UI changes, download and install the latest wxFormBuilder from the [wxFormBuilder Homepage](https://github.com/wxFormBuilder/wxFormBuilder).

You can start the VATValidation by running the following command:

```python src/VATValidation.py```

## Some screenshots

### Single validation

![single validation](images/single.png)

### Batch validation

![batch validation](images/batch.png)

### Configuration

![configuration](images/config.png)
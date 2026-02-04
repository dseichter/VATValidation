# Start development

## Start development

I am using pyenv on my computers and virtual machines.

Create and activate an environment by running the following command:

```pyenv virtualenv 3.14.2 vatvalidation-venv```

```pyenv activate vatvalidation-venv```

Install the required dependencies

```pip install -r src/requirements.txt```
```pip install -r icons/requirements.txt```
```pip install -r docs/requirements.txt```

You can start the VATValidation by running the following command:

```cd src && python vatvalidation.py```

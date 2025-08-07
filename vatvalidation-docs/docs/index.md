# VATValidation

![pep8](https://github.com/dseichter/VATValidation/actions/workflows/pep8.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validate VAT numbers using the interfaces of BZSt, VIES and/or HMRC. Provides single or batch validation with support for CSV, XLSX and JSON.

Binaries for Windows and Linux are available (see [releases](https://github.com/dseichter/VATValidation/releases)).

## Features

- 🖥️ Graphical user interface
- ✅ Single VAT number validation
- 📦 Batch processing of CSV, JSON, or XLSX
- 🇩🇪 Validation using BZSt (best, if you own a German VAT number)
- 🇪🇺 Validation using VIES
- 🇬🇧 Validation using HMRC (including VAT IDs beginning with `UK`)
- 🛠️ CLI batch processing (see [commandine](commandline.md))
- 🔒 **NO** external dependencies required

This is the successor of my VAT-Validation. Now released as Open Source.

If you like this software, please don't hesitate to give it a :star: or send me a :moneybag: donation in the amount you think the software is worth.

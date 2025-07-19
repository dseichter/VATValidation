# VATValidation

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/dseichter/VATValidation/blob/main/README.md)
[![de](https://img.shields.io/badge/lang-de-blue.svg)](https://github.com/dseichter/VATValidation/blob/main/README-de.md)

![pep8](https://github.com/dseichter/VATValidation/actions/workflows/pep8.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validate VAT numbers using the interfaces of BZSt, VIES and/or HMRC. Provides single or batch validation with support for CSV, XLSX and JSON.

Binaries for Windows and Linux are available (see releases).

## Features

* Graphical user interface
* Single validation
* Batch processing of CSV, JSON or XLSX
* Validation using BZSt (configurable, can only be used if your VAT starts with `DE`)
* Validation using VIES (configurable)
* Validation using HMRC (if you want to validate a vat starting with `UK`)
* Batch processing can be run using CLI interface (see releases)
* **NO** dependencies needed

This is the successor of my VAT-Validation. Now released as Open Source.

If you like this software, please don't hesitate to give it a :star: or send me a :moneybag: donation in the amount you think the software is worth.

## About

VATValidation supports you in validating your vat numbers based on your master data. Whether you want to check a VAT number directly at your workplace or integrate it into your ERP/CRM applications.

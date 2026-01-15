# VATValidation

![ruff](https://github.com/dseichter/VATValidation/actions/workflows/ruff.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validate VAT numbers using the interfaces of VIES and/or HMRC. Provides single or batch validation with support for CSV, XLSX and JSON.

![VATValidation](assets/single.png)

Binaries for Windows and Linux are available (see [releases](https://github.com/dseichter/VATValidation/releases)).

[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/dseichter/VATValidation/total)](https://github.com/dseichter/VATValidation/releases)
![GitHub License](https://img.shields.io/github/license/dseichter/VATValidation)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/issues)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/pulls)

## Features

- 🖥️ Graphical user interface
- ✅ Single VAT number validation
- 📦 Batch processing of CSV, JSON, or XLSX
- 🇪🇺 Validation using VIES
- 🇬🇧 Validation using HMRC (including VAT IDs beginning with `UK`)
- 🛠️ CLI batch processing (see [commandine](commandline.md))
- 🔒 **NO** external dependencies required

Since 2026 the BZSt interface has been shutdowned.

This is the successor of my VAT-Validation. Now released as Open Source.

If you like this software, please don't hesitate to give it a :star: or send me a :moneybag: donation in the amount you think the software is worth.

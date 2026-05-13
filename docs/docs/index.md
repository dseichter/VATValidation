# VATValidation

![ruff](https://github.com/dseichter/VATValidation/actions/workflows/ruff.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validate VAT numbers using the interfaces of BZSt, VIES, HMRC, and Swiss UID. Provides single or batch validation with support for CSV, XLSX and JSON.

Binaries for Windows and Linux are available (see [releases](https://github.com/dseichter/VATValidation/releases)).

[![GitHub Downloads](https://img.shields.io/github/downloads/dseichter/VATValidation/total)](https://github.com/dseichter/VATValidation/releases)
[![GitHub Stars](https://img.shields.io/github/stars/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/stargazers)
![GitHub License](https://img.shields.io/github/license/dseichter/VATValidation)
[![GitHub Open Issues](https://img.shields.io/github/issues/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/issues)
[![GitHub Open Pull Requests](https://img.shields.io/github/issues-pr/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/pulls)

## Choose Your Workflow

VATValidation can be used in three ways, depending on your workflow.

### Desktop App

Best for interactive checks and office use.

- Guide: [Graphical User Interface](gui.md)

### Automation and Scripts

Best for automation, scripting, and CI/CD.

- Guide: [Command Line](commandline.md)

### Developer Integration

Best for integrating validation into your own applications.

- Guide: [REST API](api.md)

## Quick Start

### GUI

Download and run the latest GUI binary from [releases](https://github.com/dseichter/VATValidation/releases).

### CLI

```shell
vatvalidation_cli.exe --input input.csv --output results.csv
```

On Linux:

```shell
./vatvalidation_cli --input input.csv --output results.csv
```

### API

```shell
./VATValidation-api-linux-<version> --port 8080 --proxy-mode system
```

## Features

- 🖥️ Graphical user interface
- 🛠️ CLI processing for single and batch validation
- 🌐 REST API
- ✅ Single VAT number validation
- 📦 Batch processing of CSV, JSON, or XLSX
- 🇩🇪 Validation using BZSt (German Federal Central Tax Office)
- 🇪🇺 Validation using VIES
- 🇬🇧 Validation using HMRC (including VAT IDs beginning with `UK`)
- 🇨🇭 Validation using Swiss UID (check Swiss VAT numbers)
- 🔒 No manual Python dependency installation required for release binaries

Since 2026 the old BZSt interface has been shutdown. The new BZSt API is now supported.

![VATValidation](assets/single.png)

This is the successor of my VAT-Validation. Now released as Open Source.

If you like this software, please don't hesitate to give it a :star: or send me a :moneybag: donation in the amount you think the software is worth.

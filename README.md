# VATValidation

**VATValidation** is an open-source VAT validation tool with three interfaces: GUI, CLI, and REST API. It validates VAT numbers via the official interfaces of BZSt, VIES, HMRC, and Swiss UID, and supports single and batch processing with CSV, XLSX, and JSON formats.

<p align="center">
  <img src="docs/docs/assets/select_check_box_48dp_097E23_FILL1_wght400_GRAD0_opsz48.png" alt="VATValidation Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/dseichter/VATValidation" alt="Release">
  <img src="https://img.shields.io/github/downloads/dseichter/VATValidation/total" alt="Downloads">
  <img src="https://img.shields.io/github/stars/dseichter/VATValidation" alt="Stars">
  <img src="https://img.shields.io/github/license/dseichter/VATValidation" alt="License">
</p>

<p align="center">
  <b><a href="https://dseichter.github.io/VATValidation/">Documentation</a></b> •
  <b><a href="https://github.com/dseichter/VATValidation/releases">Downloads</a></b> •
  <b><a href="https://github.com/dseichter/VATValidation/issues">Issues</a></b>
</p>

<p align="center">
<img src="https://github.com/dseichter/VATValidation/actions/workflows/ruff.yml/badge.svg" alt="ruff">
<img src="https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg" alt="bandit">
<a href="https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation"><img src="https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status" alt="Quality Gate Status"></a>
</p>

---

Binaries for Windows and Linux are available in the <a href="https://github.com/dseichter/VATValidation/releases">releases</a>.

---

## Choose Your Workflow

VATValidation can be used in three ways, depending on your workflow.

### Desktop App

Best for interactive checks and office use.

- Guide: [Graphical User Interface](https://dseichter.github.io/VATValidation/gui/)

### Automation and Scripts

Best for automation, scripting, and CI/CD.

- Guide: [Command Line](https://dseichter.github.io/VATValidation/commandline/)

### Developer Integration

Best for integrating validation into your own applications.

- Guide: [REST API](https://dseichter.github.io/VATValidation/api/)

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

## 🚀 Features

- 🖥️ Graphical user interface
- 🛠️ CLI processing for single and batch validation
- 🌐 FastAPI-based REST API
- ✅ Single VAT number validation
- 📦 Batch processing of CSV, JSON, or XLSX
- 🇩🇪 Validation using BZSt (German Federal Central Tax Office)
- 🇪🇺 Validation using VIES (EU VAT numbers)
- 🇬🇧 Validation using HMRC (check UK VAT numbers)
- 🇨🇭 Validation using Swiss UID (check Swiss VAT numbers)
- 🔒 No manual Python dependency installation required for release binaries

Since 2026 the old BZSt interface has been shutdown. The new BZSt API is now supported.

---

![VATValidation](docs/docs/assets/single.png)

---

> This is the successor of my VAT-Validation. Now released as Open Source!

If you like this software, please give it a ⭐ or send a 💰 donation in the amount you think the software is worth.

---

## 📚 Documentation

For full documentation, usage instructions, configuration, screenshots, and contributing guidelines,  
please visit the [project documentation](https://dseichter.github.io/VATValidation/).

Runtime settings are persisted in `src/config.json` (or the generated runtime config file), including proxy and logging values (`proxy_mode`, `proxy_url`, `proxy_username`, `proxy_password`, `logfilename`, `loglevel`).

---

## 📄 License

GPL 3.0 — see [LICENSE](LICENSE) file at the root of the repository for details.

## Icons

VATValidation uses [Google Material Symbols](https://fonts.google.com/icons) within its code for UI icons.  
Material Symbols are licensed under the [Apache License 2.0](https://github.com/google/material-design-icons/blob/master/LICENSE) and are free for use in open source projects.
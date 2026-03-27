# VATValidation

**VATValidation** is a powerful, open-source tool for validating VAT numbers using the official interfaces of BZSt, VIES and HMRC. It supports both single and batch validation with CSV, XLSX, and JSON formats. Including a command line interface (cli) to use it into other software, automation scripts, CI/CD pipelines, or scheduled tasks.

<p align="center">
  <img src="docs/docs/assets/select_check_box_48dp_097E23_FILL1_wght400_GRAD0_opsz48.png" alt="VATValidation Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/dseichter/VATValidation?style=flat-square" alt="Release">
  <img src="https://img.shields.io/github/downloads/dseichter/VATValidation/total?style=flat-square" alt="Downloads">
  <img src="https://img.shields.io/github/license/dseichter/VATValidation?style=flat-square" alt="License">
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

![VATValidation](docs/docs/assets/single.png)

Binaries for Windows and Linux are available in the <a href="https://github.com/dseichter/VATValidation/releases">releases</a>.

---

## 🚀 Features

- 🖥️ Graphical user interface
- ✅ Single VAT number validation
- 📦 Batch processing of CSV, JSON, or XLSX
- 🇩🇪 Validation using BZSt (German Federal Central Tax Office)
- 🇪🇺 Validation using VIES (EU VAT numbers)
- 🇬🇧 Validation using HMRC (check UK VAT numbers)
- 🇨🇭 Validation using Swiss UID (check Swiss VAT numbers)
- 🛠️ CLI batch processing (see releases)
- 🔒 No manual Python dependency installation required for release binaries

Since 2026 the old BZSt interface has been shutdown. The new BZSt API is now supported.

---

> This is the successor of my VAT-Validation. Now released as Open Source!

If you like this software, please give it a ⭐ or send a 💰 donation in the amount you think the software is worth.

---

## 📚 Documentation

For full documentation, usage instructions, configuration, screenshots, and contributing guidelines,  
please visit the [project documentation](https://dseichter.github.io/VATValidation/).

---

## 📄 License

GPL 3.0 — see [LICENSE](LICENSE) file at the root of the repository for details.

## Icons

VATValidation uses [Google Material Symbols](https://fonts.google.com/icons) within its code for UI icons.  
Material Symbols are licensed under the [Apache License 2.0](https://github.com/google/material-design-icons/blob/master/LICENSE) and are free for use in open source projects.
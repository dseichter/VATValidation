# VATValidation

![ruff](https://github.com/dseichter/VATValidation/actions/workflows/ruff.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validierung von Umsatzsteuernummern über die Schnittstellen von BZSt, VIES und/oder HMRC. Bietet Einzel- oder Batch-Validierung mit Unterstützung für CSV, XLSX und JSON.

![VATValidation](assets/single.png)

Binärdateien für Windows und Linux stehen zur Verfügung (siehe [Releases](https://github.com/dseichter/VATValidation/releases)).

[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/dseichter/VATValidation/total)](https://github.com/dseichter/VATValidation/releases)
![GitHub License](https://img.shields.io/github/license/dseichter/VATValidation)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/issues)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/dseichter/VATValidation)](https://github.com/dseichter/VATValidation/pulls)

## Merkmale

- 🖥️ Grafische Benutzeroberfläche
- ✅ Einfache Validierung
- 📦 Stapelverarbeitung von CSV, JSON oder XLSX
- 🇩🇪 Validierung mittels BZSt (Bundeszentralamt für Steuern)
- 🇪🇺 Validierung über VIES
- 🇬🇧 Validierung mit HMRC (u.a. für mit `UK` beginnende USt-Id)
- 🛠️ CLI Batch-Verarbeitung ((siehe [Kommandozeile](commandline.md)))
- 🔒**keine** Abhängigkeiten erforderlich

Seit 2026 ist die alte BZSt-Schnittstelle nicht mehr verfügbar. Die neue BZSt-API wird jetzt unterstützt.

Dies ist der Nachfolger meiner VAT-Validation. Jetzt als Open Source veröffentlicht.

Wenn Ihnen diese Software gefällt, zögern Sie bitte nicht, ihr einen :star: zu geben oder mir eine :moneybag: Spende in der Höhe zukommen zu lassen, die die Software Ihrer Meinung nach wert ist.
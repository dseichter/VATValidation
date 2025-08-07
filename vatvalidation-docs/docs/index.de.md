# VATValidation

![pep8](https://github.com/dseichter/VATValidation/actions/workflows/pep8.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validierung von Umsatzsteuernummern über die Schnittstellen von BZSt, MIAS und/oder HMRC. Bietet Einzel- oder Batch-Validierung mit Unterstützung für CSV, XLSX und JSON.

Binärdateien für Windows und Linux stehen zur Verfügung (siehe [Releases](https://github.com/dseichter/VATValidation/releases)).

## Merkmale

- 🖥️ Grafische Benutzeroberfläche
- ✅ Einfache Validierung
- 📦 Stapelverarbeitung von CSV, JSON oder XLSX
- 🇩🇪 Validierung mittels BZSt (empfohlen, wenn Sie eine dt. USt-Id besitzen)
- 🇪🇺 Validierung über VIES
- 🇬🇧 Validierung mit HMRC (u.a. für mit `UK` beginnende USt-Id)
- 🛠️ CLI Batch-Verarbeitung ((siehe [Kommandozeile](commandline.md)))
- 🔒**keine** Abhängigkeiten erforderlich

Dies ist der Nachfolger meiner VAT-Validation. Jetzt als Open Source veröffentlicht.

Wenn Ihnen diese Software gefällt, zögern Sie bitte nicht, ihr einen :star: zu geben oder mir eine :moneybag: Spende in der Höhe zukommen zu lassen, die die Software Ihrer Meinung nach wert ist.
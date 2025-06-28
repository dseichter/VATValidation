# VATValidation

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/dseichter/VATValidation/blob/main/README.md)
[![de](https://img.shields.io/badge/lang-de-blue.svg)](https://github.com/dseichter/VATValidation/blob/main/README-de.md)

![pep8](https://github.com/dseichter/VATValidation/actions/workflows/pep8.yml/badge.svg)
![bandit](https://github.com/dseichter/VATValidation/actions/workflows/bandit.yml/badge.svg)
![trivy](https://github.com/dseichter/VATValidation/actions/workflows/trivy.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dseichter_VATValidation&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dseichter_VATValidation)

Validierung von Umsatzsteuernummern über die Schnittstellen von BZSt, MIAS und/oder HMRC. Bietet Einzel- oder Batch-Validierung mit Unterstützung für CSV, XLSX und JSON.

Binärdateien für Windows und Linux stehen zur Verfügung (siehe Releases).

## Merkmale

* Grafische Benutzeroberfläche
* Einfache Validierung
* Stapelverarbeitung von CSV, JSON oder XLSX
* Validierung mittels BZSt (konfigurierbar, kann nur verwendet werden, wenn Ihre Umsatzsteuer mit `DE` beginnt)
* Validierung über VIES (konfigurierbar)
* Validierung mit HMRC (wenn Sie eine mit „UK“ beginnende Mehrwertsteuer validieren möchten)
* Batch-Verarbeitung kann über die CLI-Schnittstelle ausgeführt werden (siehe Releases)
* **keine** Abhängigkeiten erforderlich

Dies ist der Nachfolger meiner VAT-Validation. Jetzt als Open Source veröffentlicht.

Wenn Ihnen diese Software gefällt, zögern Sie bitte nicht, ihr einen :star: zu geben oder mir eine :moneybag: Spende in der Höhe zukommen zu lassen, die die Software Ihrer Meinung nach wert ist.

## Über

VATValidation unterstützt Sie bei der Validierung Ihrer Umsatzsteuernummern auf der Grundlage Ihrer Stammdaten. Egal, ob Sie eine Umsatzsteuer-Identifikationsnummer direkt an Ihrem Arbeitsplatz prüfen oder in Ihre ERP/CRM-Anwendungen integrieren wollen.

## Kommandozeilen-Tool

Wenn Sie Batch-Dateien (z.B. json, csv oder XLSX) prüfen möchten, können Sie die neuste Versionen bspw. `VATValidation-cli-windows-...exe` herunterladen und in vatvalidation_cli.exe umbenennen.

Führen Sie das Tool einfach aus, indem Sie eine Eingabe- und eine Ausgabedatei angeben. Für weitere Informationen, führen Sie bitte folgenden Befehl aus:

``vatvalidation_cli.exe``

```shell
usage: vatvalidation_cli.py [-h] [--version] --input INPUT --output OUTPUT

VAT-Validation CLI - v2024-07-06

options:
  -h, --help       show this help message and exit
  --version        show version of and exit
  --input INPUT    Input filename for VAT numbers.
  --output OUTPUT  Output filename for validation results.

For more information, visit our GitHub repository: https://github.com/dseichter/VATValidation License: GPL 3.0 - see LICENSE file at the root of the repository for details.
```

Es wird nur die Stapelverarbeitung angeboten.

## Grafische Benutzeroberfläche

VATValidation bietet eine grafische Benutzeroberfläche für Einzel- und Stapel-Validierung. Sie kann an jedem Arbeitsplatz verwendet werden und muss nicht installiert werden, und es sind keine weiteren Komponenten von Drittanbietern erforderlich.

### Einzelvalidierung

Sie können die Software an Ihrem Arbeitsplatz einsetzen und direkt gegen die offiziell unterstützten Schnittstellen von BZSt, MIAS und/oder HMRC prüfen.

![Einzelvalidierung](images/single.png "VATValidation Einzelvalidierung")

### Stapelverarbeitung

Exportieren Sie Ihre Stammdaten in eine Datei (JSON, XLSX oder CSV) und überprüfen Sie sie vollständig. Die Codepage sollte UTF-8 sein.

![Stapelverarbeitung](images/batch.png "VATValidation Stapelverarbeitung")

Die importierten Dateien müssen die folgenden Felder/Spalten enthalten. Im Falle von CSV und XLSX fügen Sie bitte die Feldnamen in die erste Zeile ein. Fügen Sie keine weiteren Spalten hinzu.

* key1
* key2
* ownvat
* foreignvat
* company
* street
* zip
* town

Die Ausgabedatei (Logfile) enthält die folgenden Informationen:

* key1
* key2
* ownvat
* foreignvat
* type
* valid
* errorcode
* errorcode_description
* valid_from
* valid_to
* timestamp
* company
* address
* town
* zip
* street

Je nach den importierten Daten und der verwendeten Schnittstelle werden einige Schlüssel keine Werte haben.

## Konfiguration

Die Konfiguration ist sehr einfach. Wechseln Sie auf die Registerkarte Konfiguration und geben Sie Ihre eigene Mehrwertsteuer ein. Diese wird für die einmalige Validierung als Standard-Mehrwertsteuer verwendet. 
Daneben können Sie Ihre Standardschnittstelle auswählen. Wenn Sie eine deutsche MwSt. besitzen, empfehlen wir die Verwendung von BZSt. Ändern Sie die Sprache Ihrer Ausgabe.

![Konfiguration](images/config.png "Konfiguration der VAT-Validierung")

Falls Sie CSV verwenden, können Sie das Trennzeichen für Ihre Import- und Exportdateien wählen.

# Bekannte Probleme

Zurzeit gibt es keine bekannten Probleme.

# Beitragen

Wenn Sie einen Beitrag leisten wollen, indem Sie einen Fehler beheben, eine neue Funktion hinzufügen oder einfach etwas optimieren, finden Sie hier eine einfache Anleitung, wie Sie mit der Entwicklung beginnen können.

## Entwicklung starten

Erstellen und aktivieren Sie eine Umgebung, indem Sie den folgenden Befehl ausführen:

```python -m venv .venv```

```.venv/Scripts/activate```

Installieren Sie die erforderlichen Abhängigkeiten

```pip install -r src/requirements.txt```

Wenn Sie einige Änderungen an der Benutzeroberfläche vornehmen möchten, laden Sie den neuesten wxFormBuilder von der [wxFormBuilder Homepage] (https://github.com/wxFormBuilder/wxFormBuilder) herunter und installieren Sie ihn.

Sie können die VATValidation starten, indem Sie den folgenden Befehl ausführen:

```python src/vatvalidation.py```

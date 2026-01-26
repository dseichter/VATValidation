# Konfiguration

Die Konfiguration ist sehr einfach. Wechseln Sie auf die Registerkarte Konfiguration und geben Sie Ihre eigene Mehrwertsteuer ein. Diese wird für die einmalige Validierung als Standard-Mehrwertsteuer verwendet. 
Daneben können Sie Ihre Standardschnittstelle auswählen. Ändern Sie die Sprache Ihrer Ausgabe.

![Konfiguration](assets/config.png "Konfiguration der VAT-Validierung")

Falls Sie CSV verwenden, können Sie das Trennzeichen für Ihre Import- und Exportdateien wählen.

## Schlüssel der Konfigurationsdatei

Die Konfiguration wird in `config.json` mit den folgenden Schlüsseln gespeichert:

| Schlüssel | Typ | Beschreibung | Beispiel |
|-----------|-----|-------------|---------|
| `delimiter` | string | Trennzeichen für CSV-Import/-Export | `"|"` |
| `interface` | string | Standardvalidierungsschnittstelle | `"vies"` |
| `language` | string | Sprache der Benutzeroberfläche | `"de"` |
| `logfilename` | string | Pfad zur Protokolldatei | `"/tmp/vatvalidation.log"` |
| `loglevel` | string | Protokollierungsstufe (DEBUG, INFO, WARNING, ERROR) | `"ERROR"` |
| `theme` | string | Anwendungsdesign (system, light, dark) | `"system"` |

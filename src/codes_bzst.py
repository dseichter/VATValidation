returncodes = [
    {
        "status": "999",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "It is currently not possible to process your request. Please try again later.",
    },
    {
        "status": "207",
        "de": "Ihnen wurde die deutsche USt-IdNr. ausschliesslich zu Zwecken der Besteuerung des innergemeinschaftlichen Erwerbs erteilt. Sie sind somit nicht berechtigt, Bestätigungsanfragen zu stellen.",
        "en": "They were granted the German VAT ID number exclusively for the purpose of taxation of intra-Community acquisitions. You are therefore not entitled to make confirmation requests.",
    },
    {
        "status": "204",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie war im Zeitraum von %validfrom bis %validto gültig.",
        "en": "The requested VAT ID number is invalid. It was valid from %validfrom to %validto.",
    },
    {
        "status": "000",
        "de": "Es wurde ein unbekannter Rückgabewert übermittelt. Bitte wenden Sie sich an support@erpware.de zur Prüfung.",
        "en": "An unknown return value was transmitted. Please send an email to support@erpware.de for verification.",
    },
    {
        "status": "202",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie ist nicht in der Unternehmerdatei des betreffenden EU-Mitgliedstaates registriert. Hinweis: Ihr Geschäftspartner kann seine gültige USt-IdNr. bei der für ihn zuständigen Finanzbehörde in Erfahrung bringen.",
        "en": "The requested VAT ID number is invalid. It is not registered in the entrepreneur file of the EU member state concerned. Note: Your business partner can obtain his valid VAT number from the tax authority responsible for him.",
    },
    {
        "status": "998",
        "de": "Sie nutzen die Testversion. Der Datensatz wurde nicht geprüft.",
        "en": "You are using the trail version. The record was not checked.",
    },
    {
        "status": "206",
        "de": "Ihre deutsche USt-IdNr. ist ungültig. Eine Bestätigungsanfrage ist daher nicht möglich. Den Grund hierfür können Sie beim Bundeszentralamt für Steuern - Dienstsitz Saarlouis - erfragen.",
        "en": "Your German VAT number is invalid. A confirmation request is therefore not possible. You can find out the reason for this from the Bundeszentralamt für Steuern - Dienstsitz Saarlouis.",
    },
    {
        "status": "217",
        "de": "Bei der Verarbeitung der Daten aus dem angefragten EU-Mitgliedstaat ist ein Fehler aufgetreten. Ihre Anfrage kann deshalb nicht bearbeitet werden.",
        "en": "An error has occurred in the processing of the data from the requested EU Member State. Your request cannot therefore be processed.",
    },
    {
        "status": "997",
        "de": "Die Anzahl der Prüfungen ist in der Testversion auf 5 beschränkt.",
        "en": "The number of exams in the trial version is limited to 5.",
    },
    {
        "status": "208",
        "de": "für die von Ihnen angefragte USt-IdNr. läuft gerade eine Anfrage von einem anderen Nutzer. Eine Bearbeitung ist daher nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "The VAT ID number you requested is currently being requested by another user. Processing is therefore not possible. Please try again later.",
    },
    {
        "status": "212",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie enthält ein unzulässiges Länderkennzeichen.",
        "en": "The requested VAT ID number is invalid. It contains an invalid country code.",
    },
    {
        "status": "201",
        "de": "Die angefragte USt-IdNr. ist ungültig.",
        "en": "The requested VAT ID number is invalid.",
    },
    {
        "status": "200",
        "de": "Die angefragte USt-IdNr. ist gültig.",
        "en": "The requested VAT ID number is valid.",
    },
    {
        "status": "205",
        "de": "Ihre Anfrage kann derzeit durch den angefragten EU-Mitgliedstaat oder aus anderen Gründen nicht beantwortet werden. Bitte versuchen Sie es später noch einmal. Bei wiederholten Problemen wenden Sie sich bitte an das Bundeszentralamt für Steuern-Dienst.",
        "en": "Your request cannot currently be answered by the requested EU Member State or for any other reason. Please try again later. In case of repeated problems, please contact the Bundeszentralamt für Steuern-Dienst (Federal Central Tax Office).",
    },
    {
        "status": "214",
        "de": "Ihre deutsche USt-IdNr. ist fehlerhaft. Sie beginnt mit 'DE' gefolgt von 9 Ziffern.",
        "en": "Your German VAT number is incorrect. It begins with 'DE' followed by 9 digits.",
    },
    {
        "status": "219",
        "de": "Bei der Durchführung der qualifizierten Bestätigungsanfrage ist ein Fehler aufgetreten. Es wurde eine einfache Bestätigungsanfrage mit folgendem Ergebnis durchgeführt: Die angefragte USt-IdNr. ist gültig.",
        "en": "An error occurred during the execution of the qualified confirmation request. A simple confirmation request was executed with the following result: The requested VAT ID number is valid.",
    },
    {
        "status": "223",
        "de": "Die angefragte USt-IdNr. ist gültig. Die Druckfunktion steht nicht mehr zur Verfügung, da der Nachweis gem. UStAE zu § 18e.1 zu führen ist.",
        "en": "The requested VAT registration number is valid. The print function is no longer available, as the proof must be provided in accordance with § 18e.1 UStAE.",
    },
    {
        "status": "213",
        "de": "Die Abfrage einer deutschen USt-IdNr. ist nicht möglich.",
        "en": "It is not possible to query a German VAT ID number.",
    },
    {
        "status": "221",
        "de": "Die Anfragedaten enthalten nicht alle notwendigen Parameter oder einen ungültigen Datentyp.",
        "en": "The request data does not contain all necessary parameters or an invalid data type.",
    },
    {
        "status": "209",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie entspricht nicht dem Aufbau der für diesen EU-Mitgliedstaat gilt.",
        "en": "The requested VAT ID number is invalid. It does not correspond to the structure that applies to this EU member state.",
    },
    {
        "status": "210",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie entspricht nicht den Prüfziffernregeln die für diesen EU-Mitgliedstaat gelten.",
        "en": "The requested VAT ID number is invalid. It does not comply with the check digit rules applicable to this EU member state.",
    },
    {
        "status": "211",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie enthält unzulässige Zeichen.",
        "en": "The requested VAT ID number is invalid. It contains invalid characters.",
    },
    {
        "status": "203",
        "de": "Die angefragte USt-IdNr. ist ungültig. Sie ist erst ab dem %validfrom gültig.",
        "en": "The requested VAT ID number is invalid. It is only valid from the %validfrom.",
    },
    {
        "status": "218",
        "de": "Eine qualifizierte Bestätigung ist zur Zeit nicht möglich. Es wurde eine einfache Bestätigungsanfrage mit folgendem Ergebnis durchgeführt: Die angefragte USt-IdNr. ist gültig.",
        "en": "A qualified confirmation is currently not possible. A simple confirmation request was made with the following result: The requested VAT ID number is valid.",
    },
    {
        "status": "215",
        "de": "Ihre Anfrage enthält nicht alle notwendigen Angaben für eine einfache Bestätigungsanfrage (Ihre deutsche USt-IdNr. und die ausl. USt-IdNr.). Ihre Anfrage kann deshalb nicht bearbeitet werden.",
        "en": "Your request does not contain all necessary information for a simple confirmation request (your German VAT ID number and the foreign VAT ID number). Your request can therefore not be processed.",
    },
    {
        "status": "216",
        "de": "Ihre Anfrage enthält nicht alle notwendigen Angaben für eine qualifizierte Bestätigungsanfrage (Ihre deutsche USt-IdNr., die ausl. USt-IdNr., Firmenname einschl. Rechtsform und Ort). Es wurde eine einfache Bestätigungsanfrage durchgeführt mit folgenden Ergebnis: Die angefragte USt-IdNr. ist gültig.",
        "en": "Your request does not contain all necessary information for a qualified confirmation request (your German VAT ID number, foreign VAT ID number, company name including legal form and location). A simple confirmation request was made with the following result: The requested VAT number is valid.",
    },
    {
        "status": "220",
        "de": "Bei der Anforderung der amtlichen Bestätigungsmitteilung ist ein Fehler aufgetreten. Sie werden kein Schreiben erhalten.",
        "en": "An error occurred when requesting the official confirmation message. You will not receive a letter.",
    },
]

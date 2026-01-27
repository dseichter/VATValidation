# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

returncodes = [
    {
        "status": "evatr-0000",
        "de": "Die angefragte Ust-IdNr. ist zum Anfragezeitpunkt gültig.",
        "en": "The requested VAT number is valid at the time of query.",
    },
    {
        "status": "evatr-0001",
        "de": "Bitte bestätigen Sie den Datenschutzhinweis.",
        "en": "Please confirm the privacy notice.",
    },
    {
        "status": "evatr-0002",
        "de": "Mindestens eins der Pflichtfelder ist nicht besetzt.",
        "en": "At least one of the required fields is not filled in.",
    },
    {
        "status": "evatr-0003",
        "de": "Die angefragte Ust-IdNr. ist zum Anfragezeitpunkt gültig. Mindestens eines der Pflichtfelder für eine qualifizierte Bestätigungsanfrage ist nicht besetzt.",
        "en": "The requested VAT number is valid at the time of query. At least one of the required fields for a qualified confirmation request is not filled in.",
    },
    {
        "status": "evatr-0004",
        "de": "Die anfragende DE Ust-IdNr. ist syntaktisch falsch. Sie passt nicht in das deutsche Erzeugungsschema.",
        "en": "The requesting German VAT number has incorrect syntax. It does not match the German generation schema.",
    },
    {
        "status": "evatr-0005",
        "de": "Die angegebene angefragte Ust-IdNr. ist syntaktisch falsch.",
        "en": "The specified requested VAT number has incorrect syntax.",
    },
    {
        "status": "evatr-0006",
        "de": "Die anfragende DE USt-IdNr. ist nicht berechtigt eine DE Ust-IdNr. anzufragen.",
        "en": "The requesting German VAT number is not authorized to query a German VAT number.",
    },
    {
        "status": "evatr-0007",
        "de": "Fehlerhafter Aufruf.",
        "en": "Incorrect call.",
    },
    {
        "status": "evatr-0008",
        "de": "Die maximale Anzahl von qualifizierten Bestätigungsabfragen für diese Session wurde erreicht. Bitte starten Sie erneut mit einer einfachen Bestätigungsabfrage.",
        "en": "The maximum number of qualified confirmation queries for this session has been reached. Please restart with a simple confirmation query.",
    },
    {
        "status": "evatr-0011",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-0012",
        "de": "Die angefragte USt-IdNr. ist syntaktisch falsch. Sie passt nicht in das Erzeugungsschema.",
        "en": "The requested VAT number has incorrect syntax. It does not match the generation schema.",
    },
    {
        "status": "evatr-0013",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-1001",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-1002",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-1003",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-1004",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-2001",
        "de": "Die angefragte USt-IdNr. ist zum Anfragezeitpunkt nicht vergeben.",
        "en": "The requested VAT number has not been assigned at the time of query.",
    },
    {
        "status": "evatr-2002",
        "de": "Die angefragte USt-IdNr. ist zum Anfragezeitpunkt nicht gültig. Sie ist erst gültig ab dem Datum im Feld gueltigAb.",
        "en": "The requested VAT number is not valid at the time of query. It is only valid from the date in the validFrom field.",
    },
    {
        "status": "evatr-2003",
        "de": "Das angegebene Länderkennzeichen der angefragten USt-IdNr. ist nicht gültig.",
        "en": "The specified country code of the requested VAT number is invalid.",
    },
    {
        "status": "evatr-2004",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-2005",
        "de": "Die angegebene eigene DE Ust-IdNr. ist zum Anfragezeitpunkt nicht gültig.",
        "en": "The specified own German VAT number is not valid at the time of query.",
    },
    {
        "status": "evatr-2006",
        "de": "Die angefragte Ust-IdNr. ist zum Anfragezeitpunkt nicht gültig. Sie war gültig im Zeitraum, der durch die Werte in den Feldern gueltigAb und gueltigBis beschrieben ist.",
        "en": "The requested VAT number is not valid at the time of query. It was valid during the period described by the values in the validFrom and validTo fields.",
    },
    {
        "status": "evatr-2007",
        "de": "Bei der Verarbeitung der Daten aus dem angefragten EU-Mitgliedstaat ist ein Fehler aufgetreten. Ihre Anfrage kann deshalb nicht bearbeitet werden.",
        "en": "An error occurred while processing data from the requested EU member state. Your request cannot be processed.",
    },
    {
        "status": "evatr-2008",
        "de": "Die angefragte Ust-IdNr. ist zum Anfragezeitpunkt gültig. Für die qualifizierte Bestätigungsanfrage liegt einer Besonderheit vor. Für Rückfragen wenden Sie sich an das BZSt.",
        "en": "The requested VAT number is valid at the time of query. There is a special case for the qualified confirmation request. For inquiries, contact the BZSt.",
    },
    {
        "status": "evatr-2011",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
    {
        "status": "evatr-3011",
        "de": "Eine Bearbeitung Ihrer Anfrage ist zurzeit nicht möglich. Bitte versuchen Sie es später noch einmal.",
        "en": "Processing of your request is not currently possible. Please try again later.",
    },
]



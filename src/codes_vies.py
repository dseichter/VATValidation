# Copyright (c) 2024-2025 Daniel Seichter
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
        "status": "TIMEOUT",
        "de": "Die Anwendung hat innerhalb der vorgegebenen Zeitspanne keine Antwort erhalten, versuchen Sie es später noch einmal.",
        "en": "The application did not receive a reply within the allocated time period, try again later.",
    },
    {
        "status": "GLOBAL_MAX_CONCURRENT_REQ",
        "de": "Ihr Antrag auf Umsatzsteuerprüfung wurde nicht bearbeitet; die maximale Anzahl gleichzeitiger Anträge wurde erreicht. Bitte senden Sie Ihre Anfrage später erneut oder kontaktieren Sie TAXUD-VIESWEB@ec.europa.eu für weitere Informationen:Ihre Anfrage kann aufgrund des hohen Traffic auf der Webanwendung nicht bearbeitet werden, bitte versuchen Sie es später noch einmal.",
        "en": "Your Request for VAT validation has not been processed; the maximum number of concurrent requests has been reached. Please re-submit your request later or contact TAXUD-VIESWEB@ec.europa.eu for further information: Your request cannot be processed due to high traffic on the web application. Please try again later.",
    },
    {
        "status": "SERVICE_UNAVAILABLE",
        "de": "Ein Fehler wurde entweder auf Netzwerkebene oder auf Webanwendungsebene festgestellt, versuchen Sie es später erneut.",
        "en": "An error was encountered either at the network level or the Web application level, try again later.",
    },
    {
        "status": "MS_UNAVAILABLE",
        "de": "Der Antrag des Mitgliedstaates ist nicht beantwortet oder nicht verfügbar. Bitte lesen Sie die Seite mit den technischen Informationen, um den Status des ersuchten Mitgliedstaates zu überprüfen, versuchen Sie es später erneut.",
        "en": "The application at the Member State is not replying or not available. Please refer to the Technical Information page to check the status of the requested Member State, try again later.",
    },
    {
        "status": "INVALID_INPUT",
        "de": "Der angegebene Ländercode ist ungültig oder die Umsatzsteuer-Identifikationsnummer ist leer.",
        "en": "The provided CountryCode is invalid or the VAT number is empty",
    },
    {
        "status": "MS_MAX_CONCURRENT_REQ",
        "de": "Ihr Antrag auf Validierung der Mehrwertsteuer wurde nicht bearbeitet; die Höchstzahl der gleichzeitigen Anträge für diesen Mitgliedstaat ist erreicht. Bitte senden Sie Ihre Anfrage später erneut oder kontaktieren Sie TAXUD-VIESWEB@ec.europa.eu für weitere Informationen: Ihre Anfrage kann aufgrund des hohen Datenverkehrs mit dem Mitgliedstaat, den Sie zu erreichen versuchen, nicht bearbeitet werden.",
        "en": "Your Request for VAT validation has not been processed; the maximum number of concurrent requests for this Member State has been reached. Please re-submit your request later or contact TAXUD-VIESWEB@ec.europa.eu for further information:Your request cannot be processed due to high traffic towards the Member State you are trying to reach. Please try again later.",
    },
]

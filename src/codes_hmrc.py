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
    {"status": "true", "de": "gültig", "en": "valid"},
    {"status": "valid", "de": "gültig", "en": "valid"},
    {"status": "invalid", "de": "ungültig", "en": "invalid"},
    {"status": "name", "de": "Firma", "en": "Company"},
    {"status": "false", "de": "ungültig", "en": "invalid"},
    {"status": "town", "de": "Ort", "en": "Town"},
    {
        "status": "TIMEOUT",
        "de": "Die Anwendung hat innerhalb der vorgegebenen Zeitspanne keine Antwort erhalten, versuchen Sie es später noch einmal.",
        "en": "The application did not receive a reply within the allocated time period, try again later",
    },
    {"status": "zip", "de": "Postleitzahl", "en": "Postalcode"},
    {
        "status": "targetVrn",
        "de": "targetVrn does not match a registered company",
        "en": "targetVrn does not match a registered company",
    },
    {
        "status": "requesterVrn",
        "de": "requesterVrn does not match a registered company",
        "en": "requesterVrn does not match a registered company",
    },
    {
        "status": "Invalid targetVrn",
        "de": "Invalid targetVrn - Vrn parameters should be 9 or 12 digits",
        "en": "Invalid targetVrn - Vrn parameters should be 9 or 12 digits",
    },
    {
        "status": "Invalid requesterVrn",
        "de": "Invalid requesterVrn - Vrn parameters should be 9 or 12 digits",
        "en": "Invalid requesterVrn - Vrn parameters should be 9 or 12 digits",
    },
    {
        "status": "Invalid targetVrn and requesterVrn",
        "de": "Invalid targetVrn and requesterVrn - Vrn parameters should be 9 or 12 digits",
        "en": "Invalid targetVrn and requesterVrn - Vrn parameters should be 9 or 12 digits",
    },
]

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

import validate_workflow

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


def validatesingle(
    key1="",
    key2="",
    ownvat="",
    foreignvat="",
    company="",
    street="",
    zip="",
    town="",
    type="vies",
    lang="en"
):
    data = {
        "key1": key1,
        "key2": key2,
        "ownvat": ownvat,
        "foreignvat": foreignvat,
        "company": company,
        "street": street,
        "zip": zip,
        "town": town,
        "type": type,
        "lang": lang,
    }
    r = validate_workflow.start_workflow(data)

    return r

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

import json
import datetime
from decimal import Decimal

import validate_vies
import validate_hmrc

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


class fakefloat(float):
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)


def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    if isinstance(o, (datetime.datetime, datetime.date)):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")


def return_fielderror(fieldname):
    return {
        "statusCode": 406,
        "body": json.dumps(
            {
                "errorcode": "VAT0001",
                "message": f"The following field is missing: {fieldname}",
            },
            default=defaultencode,
        ),
    }


def start_workflow(payload):
    logger.debug(payload)

    required_fields = ["key1", "key2", "ownvat", "foreignvat", "company", "town", "zip", "street"]
    for field in required_fields:
        if field not in payload:
            return return_fielderror(field)

    if "type" not in payload:
        payload["type"] = "vies"

    if "lang" not in payload:
        payload["lang"] = "en"

    if payload["lang"] not in ["en", "de"]:
        payload["lang"] = "en"

    # start the validation
    # Use hmrc for GB VAT numbers, otherwise use given type
    if payload["foreignvat"].upper().startswith("GB"):
        response = validate_hmrc.start_validation(payload)
    else:
        response = validate_vies.start_validation(payload)

    logger.debug(response)

    return response

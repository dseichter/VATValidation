# Copyright (c) 2024 Daniel Seichter
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
import os
import logging

import validate_bzst
import validate_vies
import validate_hmrc

logger = logging.getLogger()

# get loglevel from environment
if "LOGLEVEL" in os.environ:
    loglevel = os.environ["LOGLEVEL"]
    if loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    if loglevel == "INFO":
        logger.setLevel(logging.INFO)
    if loglevel == "ERROR":
        logger.setLevel(logging.ERROR)


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


def start_validation(payload, iscli=True):
    logger.debug(payload)

    required_fields = ["key1", "key2", "ownvat", "foreignvat", "company", "town", "zip", "street"]
    for field in required_fields:
        if field not in payload:
            return return_fielderror(field)

    if "type" not in payload:
        payload["type"] = (
            "bzst" if payload["ownvat"].upper().startswith("DE") else "vies"
        )

    if "lang" not in payload:
        payload["lang"] = "en"

    if payload["lang"] not in ["en", "de"]:
        payload["lang"] = "en"

    # start the validation
    if payload["ownvat"].upper().startswith("DE") and not payload[
        "foreignvat"
    ].upper().startswith("GB"):
        response = validate_bzst.start_validation(payload, iscli)
    elif payload["foreignvat"].upper().startswith("GB"):
        response = validate_hmrc.start_validation(payload, iscli)
    else:
        response = validate_vies.start_validation(payload, iscli)

    return response

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


def start_validation(payload):
    logger.debug(payload)

    if "key1" not in payload:
        return return_fielderror("key1")
    if "key2" not in payload:
        return return_fielderror("key2")
    if "ownvat" not in payload:
        return return_fielderror("ownvat")
    if "foreignvat" not in payload:
        return return_fielderror("foreignvat")
    if "company" not in payload:
        return return_fielderror("company")
    if "town" not in payload:
        return return_fielderror("town")
    if "zip" not in payload:
        return return_fielderror("zip")
    if "street" not in payload:
        return return_fielderror("street")

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
        response = validate_bzst.start_validation(payload)
    elif payload["foreignvat"].upper().startswith("GB"):
        response = validate_hmrc.start_validation(payload)
    else:
        response = validate_vies.start_validation(payload)

    print(response)

    return response

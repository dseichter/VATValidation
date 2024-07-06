import datetime
from decimal import Decimal
import os
import urllib3
import json
import logging

import codes_hmrc

logger = logging.getLogger()
http = urllib3.PoolManager()

URL = "https://api.service.hmrc.gov.uk/organisations/vat/check-vat-number/lookup/"

# get loglevel from environment
if "LOGLEVEL" in os.environ:
    loglevel = os.environ["LOGLEVEL"]
    if loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    if loglevel == "INFO":
        logger.setLevel(logging.INFO)
    if loglevel == "ERROR":
        logger.setLevel(logging.ERROR)

validationresult = {
    "key1": None,
    "key2": None,
    "ownvat": None,
    "foreignvat": None,
    "type": "HMRC",
    "valid": None,
    "errorcode": None,
    "errorcode_description": None,
    "valid_from": None,
    "valid_to": None,
    "errorcode_hint": None,
    "timestamp": None,
    "company": None,
    "address": None,
    "town": None,
    "zip": None,
    "street": None,
}


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


def load_codes(lang, errorcode):
    if errorcode is None:
        return None
    
    for code in codes_hmrc.returncodes:
        if code["status"] == errorcode:
            if lang == "de":
                return code["de"]
            if lang == "en":
                return code["en"]
    return None


def start_validation(payload):
    try:
        resp = http.request("GET", URL + payload["foreignvat"][2:])
        logger.debug(resp.status, resp.data)
        result = json.loads(resp.data)

        result["errorcode"] = None

        validationresult = {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": 'HMRC',
            "valid": resp.status == 200,
            "errorcode": result["errorcode"],
            "errorcode_description": load_codes(
                payload["lang"], result["errorcode"]
            ),
            "valid_from": "",
            "valid_to": "",
            "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S"
            ),
            "company": result["target"]["name"],
            "address": result["target"]["address"]["line1"]
            + chr(13)
            + result["target"]["address"]["line2"],
            "town": "",
            "zip": result["target"]["address"]["postcode"],
            "street": "",
        }

        return validationresult
    except Exception as e:
        logger.error(repr(e))
        return {"vatError": "VAT2500", "vatErrorMessage": repr(e)}

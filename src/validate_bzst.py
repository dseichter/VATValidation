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

import datetime
import urllib3
import defusedxml.minidom as minidom
import codes_bzst
import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)

http = urllib3.PoolManager()

URL = "https://evatr.bff-online.de/evatrRPC"

validationresult = {
    "key1": None,
    "key2": None,
    "ownvat": None,
    "foreignvat": None,
    "type": "BZST",
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


def gettext(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return "".join(rc)


def load_codes(lang, errorcode):
    if errorcode is None:
        return ""

    for code in codes_bzst.returncodes:
        if code["status"] == errorcode:
            return code[lang]
    return None


def start_validation(payload):
    logger.debug('-'*40)
    logger.debug('BZST')
    logger.debug('-'*40)
    logger.debug("Starting validation with payload: %s", payload)

    # map requested fields to bzst request
    bzstmap = {
        "UstId_1": payload["ownvat"],
        "UstId_2": payload["foreignvat"],
        "Firmenname": payload["company"],
        "Ort": payload["town"],
        "PLZ": payload["zip"],
        "Strasse": payload["street"],
    }
    try:
        resp = http.request("GET", URL, fields=bzstmap)
        rc = parse_response(resp.data)

        validationresult = {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": "BZST",
            "valid": is_valid(rc["ErrorCode"]),
            "errorcode": rc["ErrorCode"],
            "errorcode_description": load_codes(payload["lang"], rc["ErrorCode"]),
            "valid_from": rc["Gueltig_ab"],
            "valid_to": rc["Gueltig_bis"],
            "timestamp": get_current_timestamp(),
            "company": rc["Firmenname"],
            "address": "",
            "town": rc["Ort"],
            "zip": rc["PLZ"],
            "street": rc["Strasse"],
        }
        validationresult = substitute_variables_in_description(validationresult)
        return validationresult
    except Exception as e:
        logger.error(repr(e))
        return {"vatError": "VAT3500", "vatErrorMessage": repr(e)}


def parse_response(response_data):
    dom = minidom.parseString(response_data)
    params = dom.childNodes

    rc = {}
    for param in params:
        arrays = param.getElementsByTagName("array")
        iskey = True
        for array in arrays:
            values = array.getElementsByTagName("value")
            for value in values:
                strings = value.getElementsByTagName("string")
                if iskey:
                    iskey = False
                    for string in strings:
                        newkey = gettext(string.childNodes)
                else:
                    iskey = True
                    for string in strings:
                        newvalue = gettext(string.childNodes)
                        rc[newkey] = newvalue
    return rc


def is_valid(error_code):
    return error_code in ["200", "216"]


def get_current_timestamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def substitute_variables_in_description(payload):
    description = payload["errorcode_description"]

    description = description.replace("%validfrom", payload["valid_from"])
    description = description.replace("%validto", payload["valid_to"])

    payload["errorcode_description"] = description
    return payload

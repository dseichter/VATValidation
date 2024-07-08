import datetime
import os
import urllib3
import defusedxml.minidom as minidom
import logging
import codes_bzst

logger = logging.getLogger()
http = urllib3.PoolManager()

URL = "https://evatr.bff-online.de/evatrRPC"

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


def start_validation(payload, iscli=True):
    logger.debug(payload)

    # map requested fields to bzst request
    bzstmap = {
        "UstId_1": payload["ownvat"],
        "UstId_2": payload["foreignvat"],
        "Firmenname": payload["company"],
        "Ort": payload["town"],
        "PLZ": payload["zip"],
        "Strasse": payload["street"],
    }
    # check, if there is valid history of the vat

    try:
        resp = http.request("GET", URL, fields=bzstmap)

        dom = minidom.parseString(resp.data)

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

        validationresult = {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": "BZST",
            "valid": rc["ErrorCode"] in ["200", "216"],
            "errorcode": rc["ErrorCode"],
            "errorcode_description": load_codes(payload["lang"], rc["ErrorCode"]),
            "valid_from": rc["Gueltig_ab"],
            "valid_to": rc["Gueltig_bis"],
            "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S"
            ),
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


def substitute_variables_in_description(payload):
    description = payload["errorcode_description"]

    description = description.replace("%validfrom", payload["valid_from"])
    description = description.replace("%validto", payload["valid_to"])

    payload["errorcode_description"] = description
    return payload

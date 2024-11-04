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
from decimal import Decimal
import urllib3
import defusedxml.minidom as minidom

import codes_vies

import logging_config  # Setup the logging
import logging

logger = logging.getLogger(__name__)

http = urllib3.PoolManager()

URL = "https://ec.europa.eu/taxation_customs/vies/services/checkVatService"

validationresult = {
    "key1": None,
    "key2": None,
    "ownvat": None,
    "foreignvat": None,
    "type": "VIES",
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

HEADERS = {"Content-Type": "text/xml; charset=utf-8"}


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
        return ""

    for code in codes_vies.returncodes:
        if code["status"] == errorcode:
            return code[lang]
    return ""


def start_validation(payload):
    logger.debug('-'*40)
    logger.debug('VIES')
    logger.debug('-'*40)
    logger.debug("Starting validation with payload: %s", payload)

    foreign_vat = payload["foreignvat"]
    own_vat = payload["ownvat"]

    foreign_country_code = foreign_vat[:2]
    foreign_vat_number = foreign_vat[2:]
    own_country_code = own_vat[:2]
    own_vat_number = own_vat[2:]

    requestpayload = f"""<Envelope xmlns='http://schemas.xmlsoap.org/soap/envelope/'>
                    <Body xmlns='http://schemas.xmlsoap.org/soap/envelope/'>
                    <checkVatApprox xmlns='urn:ec.europa.eu:taxud:vies:services:checkVat:types'>
                        <countryCode>{foreign_country_code}</countryCode>
                        <vatNumber>{foreign_vat_number}</vatNumber>
                        <requesterCountryCode>{own_country_code}</requesterCountryCode>
                        <requesterVatNumber>{own_vat_number}</requesterVatNumber>
                    </checkVatApprox>
                    </Body>
                </Envelope>"""
    try:
        resp = http.request("POST", URL, headers=HEADERS, body=requestpayload)

        # example response:
        # <env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Header/><env:Body>
        #  <ns2:checkVatApproxResponse xmlns:ns2="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
        #    <ns2:countryCode>IT</ns2:countryCode><ns2:vatNumber>01739710307</ns2:vatNumber>
        #    <ns2:requestDate>2024-02-09+01:00</ns2:requestDate>
        #    <ns2:valid>false</ns2:valid>
        #    <ns2:traderName></ns2:traderName>
        #    <ns2:traderCompanyType>---</ns2:traderCompanyType>
        #    <ns2:traderAddress></ns2:traderAddress>
        #    <ns2:requestIdentifier></ns2:requestIdentifier>
        #  </ns2:checkVatApproxResponse></env:Body></env:Envelope>'
        # Faultcode
        # <env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Header/><env:Body>
        #   <env:Fault>
        #     <faultcode>env:Server</faultcode>
        #     <faultstring>MS_UNAVAILABLE</faultstring>
        # </env:Fault></env:Body></env:Envelope>
        dom = minidom.parseString(resp.data)

        logger.debug(resp.data)
        node = dom.documentElement
        result = {}
        try:
            result["traderName"] = (
                node.getElementsByTagName("ns2:traderName")[0].childNodes[0].nodeValue
            )
        except Exception as e:
            result["traderName"] = None
        try:
            result["traderAddress"] = (
                node.getElementsByTagName("ns2:traderAddress")[0]
                .childNodes[0]
                .nodeValue
            )
        except Exception as e:
            result["traderAddress"] = None
        try:
            result["valid"] = (
                node.getElementsByTagName("ns2:valid")[0].childNodes[0].nodeValue
            )
        except Exception as e:
            result["valid"] = None
        try:
            result["requestDate"] = datetime.datetime.now(
                datetime.timezone.utc
            ).strftime("%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            result["requestDate"] = None
        # in case of faultcode
        try:
            result["errorcode"] = ""
            if node.getElementsByTagName("faultstring"):
                result["errorcode"] = (
                    node.getElementsByTagName("faultstring")[0].childNodes[0].nodeValue
                )
        except Exception as e:
            result["errorcode"] = "INVALID_INPUT"

        logger.debug(result)
        # bring result in right format
        validationresult = {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": "VIES",
            "valid": result["valid"] == "true",
            "errorcode": result["errorcode"],
            "errorcode_description": load_codes(payload["lang"], result["errorcode"]),
            "valid_from": "",
            "valid_to": "",
            "timestamp": result["requestDate"],
            "company": result["traderName"],
            "address": result["traderAddress"],
            "town": "",
            "zip": "",
            "street": "",
        }
        return validationresult
    except Exception as e:
        logger.error(repr(e))
        return {"vatError": "VAT1500", "vatErrorMessage": repr(e)}

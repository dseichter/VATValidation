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

import datetime
import urllib3
import defusedxml.ElementTree as ET

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)

http = urllib3.PoolManager()
SOAP_URL = "https://www.uid-wse.admin.ch/V5.0/PublicServices.svc"

def start_validation(payload):
    """Start Swiss UID validation"""
    logger.debug('-'*40)
    logger.debug('Swiss UID')
    logger.debug('-'*40)
    logger.debug("Starting validation with payload: %s", payload)

    foreign_vat = payload["foreignvat"]
    
    # Ensure VAT number has MWST suffix
    if not foreign_vat.upper().endswith('MWST'):
        foreign_vat = f"{foreign_vat} MWST"
    
    logger.debug(f"Validating: {foreign_vat}")
    
    soap_request = f'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:uid="http://www.uid.admin.ch/xmlns/uid-wse">  <!-- NOSONAR - Standard SOAP namespace -->
  <soap:Body>
    <uid:ValidateVatNumber>
      <uid:vatNumber>{foreign_vat}</uid:vatNumber>
    </uid:ValidateVatNumber>
  </soap:Body>
</soap:Envelope>'''
    
    try:
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'http://www.uid.admin.ch/xmlns/uid-wse/IPublicServices/ValidateVatNumber'  # NOSONAR - SOAP namespace, not actual URL
        }
        
        resp = http.request(
            "POST",
            SOAP_URL,
            headers=headers,
            body=soap_request.encode('utf-8')
        )
        
        logger.debug(f"Response status: {resp.status}")
        logger.debug(f"Response data: {resp.data}")
        
        if resp.status == 200:
            root = ET.fromstring(resp.data.decode('utf-8'))
            ns = {'s': 'http://schemas.xmlsoap.org/soap/envelope/', 'uid': 'http://www.uid.admin.ch/xmlns/uid-wse'} # NOSONAR - SOAP namespace, not actual URL
            result_elem = root.find('.//uid:ValidateVatNumberResult', ns)
            
            is_valid = result_elem.text.lower() == 'true' if result_elem is not None else False
            
            validation_result = {
                "key1": payload["key1"],
                "key2": payload["key2"],
                "ownvat": payload["ownvat"],
                "foreignvat": payload["foreignvat"],
                "type": "swiss",
                "valid": is_valid,
                "errorcode": "VALID" if is_valid else "INVALID",
                "errorcode_description": "Swiss VAT number is valid" if is_valid else "Swiss VAT number is invalid",
                "valid_from": "",
                "valid_to": "",
                "timestamp": datetime.datetime.now().isoformat(),
                "company": "",
                "address": "",
                "town": "",
                "zip": "",
                "street": "",
            }
            
            return validation_result
        
        return {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": "swiss",
            "valid": False,
            "errorcode": f"HTTP_{resp.status}",
            "errorcode_description": f"Swiss UID API error: {resp.status}",
            "valid_from": "",
            "valid_to": "",
            "timestamp": datetime.datetime.now().isoformat(),
            "company": "",
            "address": "",
            "town": "",
            "zip": "",
            "street": "",
        }
        
    except Exception as e:
        logger.error(f"Swiss UID validation error: {e}")
        return {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": "swiss",
            "valid": False,
            "errorcode": "EXCEPTION",
            "errorcode_description": str(e),
            "valid_from": "",
            "valid_to": "",
            "timestamp": datetime.datetime.now().isoformat(),
            "company": "",
            "address": "",
            "town": "",
            "zip": "",
            "street": "",
        }

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

import datetime
import json
import os
import urllib3

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)

http = urllib3.PoolManager()

BASE_URL = "https://api.evatr.vies.bzst.de"
STATUS_FILE = "bzst_status.json"

def load_status_messages():
    """Load BZST status messages, update if needed"""
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Check if file is older than 24 hours
                last_update = datetime.datetime.fromisoformat(data.get('last_update', '2000-01-01'))
                if datetime.datetime.now() - last_update < datetime.timedelta(hours=24):
                    return data.get('status_messages', {})
        except Exception as e:
            logger.warning(f"Failed to load status file: {e}")
    
    # Download new status messages
    try:
        resp = http.request("GET", f"{BASE_URL}/app/v1/info/statusmeldungen")
        if resp.status == 200:
            status_data = json.loads(resp.data.decode('utf-8'))
            # Save to file
            with open(STATUS_FILE, 'w', encoding='utf-8') as f:
                json.dump({
                    'last_update': datetime.datetime.now().isoformat(),
                    'status_messages': status_data
                }, f, indent=2)
            return status_data
    except Exception as e:
        logger.error(f"Failed to download status messages: {e}")
    
    return {}

def get_status_description(status_code):
    """Get status description from loaded messages"""
    status_messages = load_status_messages()
    if isinstance(status_messages, list):
        for msg in status_messages:
            if msg.get('status') == status_code:
                return msg.get('meldung', '')
    elif isinstance(status_messages, dict):
        for msg in status_messages.get('status_messages', []):
            if msg.get('status') == status_code:
                return msg.get('meldung', '')
    return ''

def start_validation(payload):
    """Start BZST validation"""
    logger.debug('-'*40)
    logger.debug('BZST')
    logger.debug('-'*40)
    logger.debug("Starting validation with payload: %s", payload)

    foreign_vat = payload["foreignvat"]
    own_vat = payload["ownvat"]
    
    # BZST API expects specific format
    request_data = {
        "anfragendeUstid": own_vat,
        "angefragteUstid": foreign_vat,
        "firmenname": payload.get("company", ""),
        "strasse": payload.get("street", ""),
        "plz": payload.get("zip", ""),
        "ort": payload.get("town", "")
    }

    logger.debug(f"Request data: {request_data}")
    
    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        resp = http.request(
            "POST", 
            f"{BASE_URL}/app/v1/abfrage", 
            headers=headers,
            body=json.dumps(request_data)
        )
        
        logger.debug(f"Response status: {resp.status}")
        logger.debug(f"Response data: {resp.data}")
        
        # Only HTTP 200 is a success, but 4xx can still have evatr-xxxx status codes
        if resp.status == 200 or (400 <= resp.status < 500):
            try:
                result = json.loads(resp.data.decode('utf-8'))
                
                # Parse BZST response
                status_code = result.get("status", "")
                
                # Only treat as valid if status is evatr-0000, evatr-0003 or evatr-2008 AND (HTTP 200 or 400)
                is_valid = (resp.status in [200, 400]) and (status_code in ["evatr-0000", "evatr-0003", "evatr-2008"])
                
                validation_result = {
                    "key1": payload["key1"],
                    "key2": payload["key2"],
                    "ownvat": payload["ownvat"],
                    "foreignvat": payload["foreignvat"],
                    "type": "bzst",
                    "valid": is_valid,
                    "errorcode": status_code,
                    "errorcode_description": get_status_description(status_code,),
                    "valid_from": result.get("gueltigAb", ""),
                    "valid_to": result.get("gueltigBis", ""),
                    "timestamp": datetime.datetime.now().isoformat(),
                    "company": result.get("ergFirmenname", ""),
                    "address": result.get("address", ""),
                    "town": result.get("ergOrt", ""),
                    "zip": result.get("ergPlz", ""),
                    "street": result.get("ergStrasse", ""),
                }
                
                return validation_result
            except json.JSONDecodeError:
                logger.warning(f"Failed to parse JSON response for status {resp.status}")
        
        # Handle other error statuses (5xx, etc.)
        error_msg = f"BZST API error: {resp.status}"
        try:
            error_data = json.loads(resp.data.decode('utf-8'))
            error_msg = error_data.get('message', error_msg)
        except Exception as e:
            logger.warning(f"Failed to parse error response: {e}")
        
        # Set valid to "n/a" for 5xx server errors
        valid_status = "n/a" if 500 <= resp.status < 600 else False
        
        return {
                "key1": payload["key1"],
                "key2": payload["key2"],
                "ownvat": payload["ownvat"],
                "foreignvat": payload["foreignvat"],
                "type": "bzst",
                "valid": valid_status,
                "errorcode": f"HTTP_{resp.status}",
                "errorcode_description": error_msg,
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
        logger.error(f"BZST validation error: {e}")
        return {
            "key1": payload["key1"],
            "key2": payload["key2"],
            "ownvat": payload["ownvat"],
            "foreignvat": payload["foreignvat"],
            "type": "bzst",
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
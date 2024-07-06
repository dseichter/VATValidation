import boto3
import datetime
from decimal import Decimal
import os
import urllib3
import json
import logging

logger = logging.getLogger()
http = urllib3.PoolManager()

TABLENAME = os.environ['DYNAMODB']
TABLENAME_CODES = os.environ['DYNAMODB_CODES']
URL = os.environ['URL']
TYPE = os.environ['TYPE']

# get loglevel from environment
if 'LOGLEVEL' in os.environ:
    loglevel = os.environ['LOGLEVEL']
    if loglevel == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    if loglevel == 'INFO':
        logger.setLevel(logging.INFO)
    if loglevel == 'ERROR':
        logger.setLevel(logging.ERROR)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLENAME)
codes = dynamodb.Table(TABLENAME_CODES)

validationresult = {
    "key1": None,
    "key2": None,
    "ownvat": None,
    "foreignvat": None,
    "type": TYPE,
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
    "street": None
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

    response = codes.get_item(Key={
        'status': errorcode
    })

    if 'Item' in response:
        if 'de' in response['Item'] and lang == 'de':
            return response['Item']['de']
        if 'en' in response['Item'] and lang == 'en':
            return response['Item']['en']

    return None


def save_validation(result, rawdata=None):
    today = datetime.date.today()
    try:
        logger.debug('before db')
        table.update_item(
            Key={"vat": result['foreignvat'], "date": today.strftime("%Y-%m-%d") + "|" + result['type']},
            UpdateExpression="""
            set validationtimestamp=:validationtimestamp,
                checktype=:checktype,
                valid=:valid,
                errorcode=:errorcode,
                valid_from=:valid_from,
                valid_to=:valid_to,
                company=:company,
                address=:address,
                town=:town,
                zip=:zip,
                street=:street,
                rawdata=:rawdata
            """,
            ExpressionAttributeValues={":validationtimestamp": result['timestamp'],
                                       ":checktype": result['type'],
                                       ":valid": result['valid'],
                                       ":errorcode": result['errorcode'],
                                       ":valid_from": result['valid_from'],
                                       ":valid_to": result['valid_to'],
                                       ":company": result['company'],
                                       ":address": result['address'],
                                       ":town": result['town'],
                                       ":zip": result['zip'],
                                       ":street": result['street'],
                                       ":rawdata": rawdata
                                       },
            ReturnValues="UPDATED_NEW",
        )
        logger.debug('after db')
    except Exception as e:
        logger.error(repr(e))
        return False

    return True


def lambda_handler(event, context):  # NOSONAR

    logger.debug(event)
    requestfields = event
    # read the values from the payload

    # check, if there is valid history of the vat

    try:
        resp = http.request("GET", URL + requestfields['foreignvat'][2:])
        logger.debug(resp.status, resp.data)
        result = json.loads(resp.data)

        result['errorcode'] = None

        validationresult = {
            'key1': requestfields['key1'],
            'key2': requestfields['key2'],
            'ownvat': requestfields['ownvat'],
            'foreignvat': requestfields['foreignvat'],
            'type': TYPE,
            'valid': resp.status == 200,
            'errorcode': result['errorcode'],
            'errorcode_description': load_codes(requestfields['lang'], result['errorcode']),
            'valid_from': '',
            'valid_to': '',
            'timestamp': datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            'company': result['target']['name'],
            'address': result['target']['address']['line1'] + chr(13) + result['target']['address']['line2'],
            'town': '',
            'zip': result['target']['address']['postcode'],
            'street': ''
        }

        # save only, if response itself is valid
        if resp.status == 200:
            save_validation(validationresult, rawdata=resp.data.decode('utf-8'))

        return validationresult
    except Exception as e:
        logger.error(repr(e))
        return {'vatError': 'VAT2500', 'vatErrorMessage': repr(e)}

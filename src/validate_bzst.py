import boto3
import datetime
from decimal import Decimal
import os
import urllib3
from xml.dom import minidom
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

HEADERS = {
    'Content-Type': 'text/xml; charset=utf-8'
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

    # optimize the request

    foreign_vat = requestfields['foreignvat']
    own_vat = requestfields['ownvat']

    foreign_country_code = foreign_vat[:2]
    foreign_vat_number = foreign_vat[2:]
    own_country_code = own_vat[:2]
    own_vat_number = own_vat[2:]

    payload = f"""<Envelope xmlns='http://schemas.xmlsoap.org/soap/envelope/'>
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
        resp = http.request("POST", URL, headers=HEADERS, body=payload)

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
            result['traderName'] = node.getElementsByTagName('ns2:traderName')[0].childNodes[0].nodeValue
        except Exception as e:
            result['traderName'] = None
        try:
            result['traderAddress'] = node.getElementsByTagName('ns2:traderAddress')[0].childNodes[0].nodeValue
        except Exception as e:
            result['traderAddress'] = None
        try:
            result['valid'] = node.getElementsByTagName('ns2:valid')[0].childNodes[0].nodeValue
        except Exception as e:
            result['valid'] = None
        try:
            result['requestDate'] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            result['requestDate'] = None
        # in case of faultcode
        try:
            result['errorcode'] = node.getElementsByTagName('faultstring')[0].childNodes[0].nodeValue
        except Exception as e:
            result['errorcode'] = None

        logger.debug(result)
        # bring result in right format
        validationresult = {
            'key1': requestfields['key1'],
            'key2': requestfields['key2'],
            'ownvat': requestfields['ownvat'],
            'foreignvat': requestfields['foreignvat'],
            'type': TYPE,
            'valid': result['valid'] == "true",
            'errorcode': result['errorcode'],
            'errorcode_description': load_codes(requestfields['lang'], result['errorcode']),
            'valid_from': '',
            'valid_to': '',
            'timestamp': result['requestDate'],
            'company': result['traderName'],
            'address': result['traderAddress'],
            'town': '',
            'zip': '',
            'street': ''
        }

        # save only, if response itself is valid
        if resp.status == 200:
            save_validation(validationresult, rawdata=resp.data.decode('utf-8'))

        return validationresult
    except Exception as e:
        logger.error(repr(e))
        return {'vatError': 'VAT1500', 'vatErrorMessage': repr(e)}

import boto3
import json
import datetime
from decimal import Decimal
import os
import logging

logger = logging.getLogger()

STEPFUNCTION = os.environ['STEPFUNCTION']
# get loglevel from environment
if 'LOGLEVEL' in os.environ:
    loglevel = os.environ['LOGLEVEL']
    if loglevel == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    if loglevel == 'INFO':
        logger.setLevel(logging.INFO)
    if loglevel == 'ERROR':
        logger.setLevel(logging.ERROR)

sf = boto3.client('stepfunctions', region_name='eu-central-1')


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
        'statusCode': 406,
        'body': json.dumps({'errorcode': 'VAT0001', 'message': f"The following field is missing: {fieldname}"},
                           default=defaultencode)
    }


def lambda_handler(event, context):  # NOSONAR

    logger.debug(event)
    payload = json.loads(event['body'])

    if 'key1' not in payload:
        return return_fielderror('key1')
    if 'key2' not in payload:
        return return_fielderror('key2')
    if 'ownvat' not in payload:
        return return_fielderror('ownvat')
    if 'foreignvat' not in payload:
        return return_fielderror('foreignvat')
    if 'company' not in payload:
        return return_fielderror('company')
    if 'town' not in payload:
        return return_fielderror('town')
    if 'zip' not in payload:
        return return_fielderror('zip')
    if 'street' not in payload:
        return return_fielderror('street')

    if 'type' not in payload:
        payload['type'] = 'bzst' if payload['ownvat'].upper().startswith('DE') else 'vies'

    if 'lang' not in payload:
        payload['lang'] = 'en'

    if payload['lang'] not in ['en', 'de']:
        payload['lang'] = 'en'

    # trigger stepfunction
    try:
        response = sf.start_sync_execution(
            stateMachineArn=STEPFUNCTION,
            name=payload['foreignvat'],
            input=json.dumps(payload)
        )
        logger.debug(response)
        if response['status'] == 'SUCCEEDED' and 'output' in response:
            result = json.loads(response['output'])
            if 'vatError' not in result:
                return {
                    'statusCode': 200,
                    'body': response['output']
                }
            else:
                return {
                    'statusCode': 500,
                    'body': response['output']
                }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'errorcode': 'VAT0400', 'errormessage': response})
            }
    except Exception as e:
        logger.error(repr(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'errorcode': 'VAT0500', 'errormessage': repr(e)}, default=defaultencode)
        }

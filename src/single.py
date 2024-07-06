import helper

import urllib3
import json


def validatesingle(key1='',
                   key2='',
                   ownvat='',
                   foreignvat='',
                   company='',
                   street='',
                   zip='',
                   town='',
                   type='vies',
                   lang='en'):

    # create POST request with all input parameters
    http = urllib3.PoolManager()
    url = helper.load_value_from_json_file('url')
    headers = {'Content-Type': 'application/json'}
    data = {
        'key1': key1,
        'key2': key2,
        'ownvat': ownvat,
        'foreignvat': foreignvat,
        'company': company,
        'street': street,
        'zip': zip,
        'town': town,
        'type': type,
        'lang': lang
    }
    r = http.request('POST', url, headers=headers, body=json.dumps(data))
    return r.status, r.data

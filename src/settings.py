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

import json
import tempfile

CONFIGFILE = 'config.json'


# load value from json file with given key
def load_value_from_json_file(key):
    with open("config.json", "r") as f:
        data = json.load(f)

    if key not in data:
        return None

    return data[key]


def create_config():
    # create the config file if it does not exist
    try:
        with open(CONFIGFILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(CONFIGFILE, 'w') as f:
            f.write('{}')

    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    # add missing keys
    if 'logfilename' not in data:
        log_dir = tempfile.gettempdir()
        data['logfilename'] = f'{log_dir}/vatvalidation.log'
    if 'loglevel' not in data:
        data['loglevel'] = 'ERROR'

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def read_config():
    with open(CONFIGFILE, 'r') as f:
        return json.load(f)


def save_config(key, value):
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)
        data[key] = value
    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

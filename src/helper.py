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

import urllib3
import json
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

VERSION = "v2025-06-28"
UPDATEURL = 'https://api.github.com/repos/dseichter/VATValidation/releases/latest'
RELEASES = 'https://github.com/dseichter/VATValidation/releases'
NAME = 'VATValidation'
LICENCE = 'GPL-3.0'


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', UPDATEURL)
        data = json.loads(r.data.decode('utf-8'))
        latest_version = data['tag_name']
        return latest_version != VERSION
    except Exception as e:
        logging.error(f"Error checking for new release: {e}")
        return False

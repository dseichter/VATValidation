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

import urllib3
import json
import logging
from packaging import version

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

VERSION = "v2026-02-15"
UPDATEURL = 'https://api.github.com/repos/dseichter/VATValidation/releases/latest'
RELEASES = 'https://github.com/dseichter/VATValidation/releases'
NAME = 'VATValidation'
LICENCE = 'GPL-3.0'


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', UPDATEURL)
        releases = json.loads(r.data.decode('utf-8'))
        # Find the latest stable (not prerelease) release
        for release in releases:
            if not release.get('prerelease', False):
                latest_version = release.get('tag_name')
                return version.parse(latest_version) > version.parse(VERSION)
        return False  # No stable release found
    except Exception as e:
        logging.error(f"Error checking for new release: {e}")
        return False

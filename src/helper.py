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
from packaging import version

VERSION = "v2026-01-02"
UPDATEURL = 'https://api.github.com/repos/dseichter/Workdir/releases/latest'
RELEASES = 'https://github.com/dseichter/Workdir/releases'
NAME = 'Workdir'
LICENCE = 'GPL-3.0'


def normalize_version_tag(tag: str) -> str:
    normalized = tag.strip()
    if normalized.lower().startswith('v'):
        normalized = normalized[1:]
    return normalized.replace('-', '.')


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', UPDATEURL)
        release = json.loads(r.data.decode('utf-8'))

        if isinstance(release, list):
            latest_release = next((item for item in release if not item.get('prerelease', False)), None)
        elif isinstance(release, dict):
            latest_release = None if release.get('prerelease', False) else release
        else:
            return False

        if latest_release is None:
            return False

        latest_version = latest_release.get('tag_name')
        if not latest_version:
            return False

        return version.parse(normalize_version_tag(latest_version)) > version.parse(normalize_version_tag(VERSION))
    except Exception as e:
        logging.error(f"Error checking for new release: {e}")
        return False

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

import json
import os

CONFIGFILE = os.path.join(os.path.expanduser('~'), '.workdir', 'config.json')
os.makedirs(os.path.dirname(CONFIGFILE), exist_ok=True)


def _default_command(cmd: str) -> dict:
    return {
        'label': 'CMD' if cmd == 'CMD1' else '',
        'command': 'cmd' if cmd == 'CMD1' else '',
        'parameters': '/k "cd {directory}"' if cmd == 'CMD1' else '',
        'use_env': False,
        'confirmation': False,
        'colour': '#000000',
    }


def _ensure_base_settings(data: dict) -> None:
    if 'directories' not in data or len(data['directories']) == 0:
        data['directories'] = [os.path.expanduser("~")]

    if 'env' not in data:
        data['env'] = []

    if 'minimize_to_tray' not in data:
        data['minimize_to_tray'] = True


def _ensure_command_defaults(data: dict) -> None:
    for cmd in ['CMD1', 'CMD2', 'CMD3', 'CMD4', 'CMD5', 'CMD6']:
        if cmd not in data:
            data[cmd] = _default_command(cmd)


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

    _ensure_base_settings(data)
    _ensure_command_defaults(data)

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def load_command(key):
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    if key not in data:
        return None

    return data[key]


# load value from json file with given key
def load_env_vars():
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    if 'env' not in data:
        return None

    return data['env']


# load directories
def load_directories():
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    if 'directories' not in data:
        return None

    return data['directories']


# save directories
def save_directories(directories):
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    # remove empty directories
    directories = [d for d in directories if d != '']

    data['directories'] = directories

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


# save environment variables
def save_env_vars(env):
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    # remove empty env vars
    env = [e for e in env if e != '']

    data['env'] = env

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


# save command
def save_command(key, cmd):
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    data[key] = cmd

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def load_minimize_to_tray() -> bool:
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    return bool(data.get('minimize_to_tray', True))


def save_minimize_to_tray(value: bool) -> None:
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    data['minimize_to_tray'] = bool(value)

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

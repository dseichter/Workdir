import json

CONFIGFILE = 'config.json'


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

    if 'directories' not in data:
        data['directories'] = []

    if 'env' not in data:
        data['env'] = []

    for cmd in ['CMD1', 'CMD2', 'CMD3', 'CMD4', 'CMD5', 'CMD6']:
        if cmd not in data:
            data[cmd] = {}
            data[cmd]['label'] = 'CMD' if cmd == 'CMD1' else ''
            data[cmd]['command'] = 'cmd' if cmd == 'CMD1' else ''
            data[cmd]['parameters'] = '/k "cd {directory}"' if cmd == 'CMD1' else ''
            data[cmd]['use_env'] = False
            data[cmd]['confirmation'] = False
            data[cmd]['colour'] = '#000000'

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

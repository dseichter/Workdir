import json


def load_command(key):
    with open('config.json', 'r') as f:
        data = json.load(f)

    if key not in data['commands']:
        return None

    return data['commands'][key]

# load value from json file with given key
def load_env_vars():
    with open('config.json', 'r') as f:
        data = json.load(f)

    if 'env' not in data:
        return None

    return data['env']

# load directories
def load_directories():
    with open('config.json', 'r') as f:
        data = json.load(f)

    if 'directories' not in data:
        return None

    return data['directories']

# save directories
def save_directories(directories):
    with open('config.json', 'r') as f:
        data = json.load(f)

    data['directories'] = directories

    with open('config.json', 'w') as f:
        json.dump(data, f)
        
# save environment variables
def save_env_vars(env):
    with open('config.json', 'r') as f:
        data = json.load(f)

    data['env'] = env

    with open('config.json', 'w') as f:
        json.dump(data, f)
        
# save command
def save_command(key, cmd):
    with open('config.json', 'r') as f:
        data = json.load(f)

    data['commands'][key] = cmd

    with open('config.json', 'w') as f:
        json.dump(data, f)
        
    

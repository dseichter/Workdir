import json


def create_config():
    with open('config.json', 'r') as f:
        data = json.load(f)
        
    if 'directories' not in data:
        data['directories'] = []
        
    if 'env' not in data:
        data['env'] = []
        
    for cmd in ['CMD1', 'CMD2', 'CMD3', 'CMD4', 'CMD5', 'CMD6']:
        if cmd not in data:
            data[cmd] = {}
            data[cmd]['label'] = ''
            data[cmd]['command'] = ''
            data[cmd]['parameters'] = ''
            data[cmd]['use_env'] = False
            data[cmd]['confirmation'] = False
            data[cmd]['colour'] = '#000000'
            
    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)            
    

def load_command(key):
    with open('config.json', 'r') as f:
        data = json.load(f)

    if key not in data:
        return None

    return data[key]

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
        json.dump(data, f, indent=4, sort_keys=True)    
        
# save environment variables
def save_env_vars(env):
    with open('config.json', 'r') as f:
        data = json.load(f)

    data['env'] = env

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)    
        
# save command
def save_command(key, cmd):
    with open('config.json', 'r') as f:
        data = json.load(f)

    data[key] = cmd

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)    

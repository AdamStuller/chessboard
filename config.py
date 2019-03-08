

__config_values = {
    "limit" : 10000,
    "width" : 5,
    "height": 5
}

def get(key: str): 
    try:
        return __config_values[key]
    except KeyError:
        return False
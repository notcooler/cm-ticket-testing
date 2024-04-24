import json

def getConfig():
    with open('./configs/config.json') as f:
        config = json.load(f)
    return config

def getSearchConfig():
    with open('./configs/searchConfig.json') as f:
        config = json.load(f)
    return config

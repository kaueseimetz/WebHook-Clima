import json

def getConfig():
    with open("config.json") as ctf:
        data = json.load(ctf)
    return data

Config = getConfig()
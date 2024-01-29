import json

with open("config.json") as ctf:
    data = json.load(ctf)

def WeatherKey():
    return data['WeatherAPI_Key']
def WebhookURL():
    return data['WebHook_URL']

import requests, json, utf8

class weather:
    def __init__(self):        
        self.API_Key=""
        
    def getWeather(self, country):
        request = requests.get(f"http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/{country}?token={self.API_Key}")

        return request.content
        

def getLastWeather():            
    clima = weather()

    with open("config.json", "r") as ctf:
        data = json.load(ctf)

    clima.API_Key = data["WeatherAPI_Key"]

    weather_content = json.loads(clima.getWeather("BR").decode('utf-8'))
    
#    weather_analysis = weather_content[0]['text']
#    weather_date = weather_content[0]['date']
#    weather_country = weather_content[0]['country']
    
    return weather_content



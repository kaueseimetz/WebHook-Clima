from webhook import webhook
from config import Config
import weather

wh = webhook(URL=Config['WebHook_URL'])

embeded_clima = {
    "content": "",
    "embeds": [
        {
            "title": "Ultimas noticias sobre o clima no Brasil",
            "description": weather.getLastWeather()[0]['text'],
            "color": 41663  
        }
    ]
}

message = wh.send_embeded_message(embeded_clima)

print(message.text)

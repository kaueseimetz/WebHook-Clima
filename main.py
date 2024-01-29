from webhook import webhook
import weather, config


wh = webhook(URL=config.WebhookURL())

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

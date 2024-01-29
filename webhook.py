import requests, json

class webhook():
    def __init__(self, URL):
        self.url = URL
    
    def send_plain_message(self, plain_message):
        
        data = {"content": json.dumps(plain_message)}
        
        response = requests.post(self.url, json=data)
        
        return response
    
    def send_embeded_message(self, embeded_message):
        response = requests.post(self.url, json=embeded_message)
        return response
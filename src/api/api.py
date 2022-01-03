import requests
from datetime import datetime

class Crypto:

    def __init__(self,name):
        self.name = name
        self.api = requests.get(f"https://sochain.com//api/v2/get_price/{self.name}")
        self.json_api = self.api.json()


    def price(self):

        for coin in self.json_api['data']['prices']:

            if coin.get('price_base') == 'USD' :
                print(datetime.utcfromtimestamp(int(coin.get('time'))).strftime('%Y-%m-%d %H:%M:%S'))
                print('-'*50)
                print(f"{self.name} price:{coin.get('price')} Dollar")

            if coin.get('price_base') == 'EUR' :
                print(f"{self.name} price:{coin.get('price')} Euro")
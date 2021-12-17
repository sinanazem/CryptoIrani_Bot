import requests

def doge():
    api = requests.get("https://sochain.com//api/v2/get_price/DOGE")
    j_api = api.json()
    name = j_api['data']['network']
    btc,usd = dict(),dict()
    for coin in j_api['data']['prices']:

        if coin['price_base'] == 'BTC' :
            btc['price_base'] = coin['price_base']
            btc['price'] = coin['price']

        if coin['price_base'] == 'USD' :
            usd['price_base'] = coin['price_base']
            usd['price'] = coin['price']

        return f"The price of {name} is {usd['price']} dollars."


def btc():
    api = requests.get("https://sochain.com//api/v2/get_price/BTC")
    j_api = api.json()
    name = j_api['data']['network']
    btc,usd = dict(),dict()
    for coin in j_api['data']['prices']:

        if coin['price_base'] == 'BTC' :
            btc['price_base'] = coin['price_base']
            btc['price'] = coin['price']

        if coin['price_base'] == 'USD' :
            usd['price_base'] = coin['price_base']
            usd['price'] = coin['price']

        return f"The price of {name} is {usd['price']} dollars."


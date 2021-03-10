import requests
import json


def get_input():
    return str(input()).lower()


def get_text_request(url_):
    r = requests.get(url_)
    if r:
        return r.text
    else:
        return None


from_currency = get_input()
cache = dict()
url = 'https://www.floatrates.com/daily/' + from_currency + '.json'
response = get_text_request(url)
currency = json.loads(response)

if from_currency != 'usd':
    cache['usd'] = currency['usd']['rate']

if from_currency != 'eur':
    cache['eur'] = currency['eur']['rate']

while True:
    to_currency = get_input()

    if to_currency == '':
        break
    else:
        amount = int(input())

    print('Checking the cache...')

    if to_currency in cache:
        print('Oh! It is in the cache!')
        print(f'You received {round(cache[to_currency] * amount, 2)} {to_currency.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        cache[to_currency] = currency[to_currency]['rate']
        print(f'You received {round(cache[to_currency] * amount, 2)} {to_currency.upper()}.')

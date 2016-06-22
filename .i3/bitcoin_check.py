
import requests


def check():
    # get BTC info
    priceUSD = 'a lot '
    blocks = ''
    info = ''
    response = requests.get(
        'https://chain.so/api/v2/get_info/BTC', verify=True)
    if response.status_code == 200:
        info = response.json()
        name = info['data']['name']
        network = info['data']['network']
        blocks = info['data']['blocks']
        blocks = str(blocks)  # needs to be a string for curses to display
    # get USD prices, exchange is Coinbase
    response = requests.get(
        'https://chain.so/api/v2/get_price/BTC/USD', verify=True)
    if response.status_code == 200:
        info = response.json()
        exchangeUSD = info['data']['prices'][1]['exchange']
        currencyUSD = info['data']['prices'][1]['price_base']
        priceUSD = info['data']['prices'][1]['price']
        priceUSD = float(priceUSD)
    # get EUR prices, exchange is BTC-E
    response = requests.get(
        'https://chain.so/api/v2/get_price/BTC', verify=True)
    if response.status_code == 200:
        info = response.json()
        # exchangeEUR = info['data']['prices'][0]['exchange']
        # currencyEUR = info['data']['prices'][0]['price_base']
        # priceEUR = info['data']['prices'][0]['price']

    return priceUSD, blocks,  info


def dollar():
    value = 0
    url = 'http://cotacoes.economia.uol.com.br/cambioJSONChart.html'
    response = requests.get(url, verify=True)
    if response.status_code == 200:
        info = response.json()
        open = info[2]['open'] != '0'
        value = float(info[2]['ask'])

    return value

if __name__ == '__main__':
    from sys import argv
    # if len(argv) > 1:
    btc = check()[0]
    usd = dollar()
    print(" 1 = R${:.3f}".format(btc * usd), end='  ')
    print("1$ = R${:.3f} ".format(dollar()))

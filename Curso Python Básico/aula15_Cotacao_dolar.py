import requests
import json
import time
import datetime

while True:
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = json.loads(requisicao.text)

    print('#### COTAÇÃO #### -', datetime.datetime.now())
    print('Dólar: R$', cotacao['USDBRL']['high'])
    print('Euro: R$', cotacao['EURBRL']['high'])
    print('BitCoin: R$', cotacao['BTCBRL']['high'])
    time.sleep(5)
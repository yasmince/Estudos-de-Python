import requests

try:
    requisicao = requests.get('http://g1.com.br')
    print(requisicao.text)

except Exception as e:
    print('Resquisição deu erro:', e)
import re
import requests

requisicao = requests.get('http://lacoxinha.com.br/contato')


padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) # RAW String

if padrao:
    print(padrao)
else:
    print('Padrão não foi encontrado')
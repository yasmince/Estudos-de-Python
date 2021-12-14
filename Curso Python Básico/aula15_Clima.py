import requests
import json

cidade = input('Escreve a sua cidade: ')

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=096c6513f95035fe258607f3c9a873d6')
tempo = json.loads(requests.text)
print('Condição do tempo: ', tempo['weather'][0]['main'])
print('Temperatura: ' + ((float(tempo['main']['temp']) - 32) / 1.8) + 'ºC' )
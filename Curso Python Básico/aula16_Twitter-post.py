import oauth2
import json
import urllib.parse
cosumer_key = 'efyI4HH0nIIelVQiFE28wx9q2'
consumer_secret = 'k9ofoNDpVBHcGn1IM3FbLTEIqP2aBVMbuhjhwjDN3hRc8p9g28'

token_key = '1386029505253449730-5CQoYY21K2w498MegKQqOLhxx2uJfs'
token_secret = 'hvbNNFELmiHZ7nV2FqrussmpDC8VVlSSoyUA1eGVB5pw8'

consumer = oauth2.Consumer(cosumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input('Novo Tweet: ')
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)

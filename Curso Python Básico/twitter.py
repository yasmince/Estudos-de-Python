import oauth2
import urllib
import json

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):

        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):

        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(consumer, token)

    def tweet(self, novo_tweet):

        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, query):

        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['statuses']
        return tweets
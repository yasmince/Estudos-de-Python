from twitter import Twitter

consumer_key = 'efyI4HH0nIIelVQiFE28wx9q2'
consumer_secret = 'k9ofoNDpVBHcGn1IM3FbLTEIqP2aBVMbuhjhwjDN3hRc8p9g28'

token_key = '1386029505253449730-5CQoYY21K2w498MegKQqOLhxx2uJfs'
token_secret = 'hvbNNFELmiHZ7nV2FqrussmpDC8VVlSSoyUA1eGVB5pw8'

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

#resp = twitter.tweet('')

pesquisa = twitter.search('solyd')

for resultado in pesquisa:

    print(resultado['text'])
    print(resultado['user']['screen_name'])
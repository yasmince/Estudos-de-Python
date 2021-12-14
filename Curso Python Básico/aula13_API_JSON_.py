import requests
import json

def requisicao (titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&tipe=movie')
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes (filme):
    print('Titulo:', filme['Title'])

    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('')

sair = False
while not sair:
    op = input('Escreve o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)
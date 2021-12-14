import requests
import json


def listafilmes(titulo):

    lista = []
    for i in range(1, 100):

        try:

            print('Pesquisando na página: ', i)
            req = requests.get('http://www.omdbapi.com/?s=' + titulo + '&type=movie&page='+ str(i))
            resposta = json.loads(req.text)

            if resposta['Response'] == 'False':

                print('Fim das páginas')
                break

            else:

                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + ' (' + ano +')'
                    lista.append(string)

        except:
            print('Conexão Falhou')

    return lista

sair = False
while not sair:
    op = input('Insira o nome do fime que deseja procurar ou digite SAIR: ')
    if op == 'SAIR':
        sair = True
    else:
        lista_de_filmes = listafilmes(op)
        print('Filmes encontrados: ', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)
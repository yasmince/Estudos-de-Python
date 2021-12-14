## Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa. O programa deve perguntar os nomes, colocar em uma lista e printar na tela, com o final da execuçaõ

qtd_pessoas = input('Informe a quantidade de pessoas que serao convidadas: ')
nomes = []
i = 1

while i <= int(qtd_pessoas):
    nome = input('Insira o nome do covidado #'+ str(i) +': ')
    nomes.append (nome)
    i += 1

for convidado in nomes:
    print(convidado)
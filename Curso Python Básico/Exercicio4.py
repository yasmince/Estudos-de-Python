## Escreva uma função que recebe um objeto de coleção e vai retornar o valor do maior númeor dentro dessa coleção
## Faça também uma função que retorna o menor valor

def maior(var):
    maior = var[0]
    for item in var:
        if item > maior:
            maior = item
    return maior

def menor(var):
    menor = var[0]
    for item in var:
        if item < menor:
            menor = item
    return menor

print(maior([0,8,20,3500,2,5,280]))
print(menor([0,8,20,3500,2,5,280]))
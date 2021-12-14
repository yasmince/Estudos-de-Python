tamanho_area = float(input("Qual o tamanho em metro quadrado a ser pintado: "))
lata = 18

qtd_litro = tamanho_area/3
qtd_latas = qtd_litro/18
valor_pagar = qtd_latas * 80

print ('A quantidade de latas necessarias e: ', qtd_latas, 'O valor a ser pago e: R$', valor_pagar)
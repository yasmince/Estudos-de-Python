altura = float(input("Insira a altura: "))
sexo = input("Insira o sexo: ")

if sexo == 'mulher':
	peso_ideal = (62.1*altura) - 44.7
	print("Seu peso ideal e: ", peso_ideal, "Kg")

if sexo == 'homem':
	peso_ideal = (72.7*altura) - 58
	print("Seu peso ideal e: ", peso_ideal, "Kg")

else:
	print("Opcao invalida")



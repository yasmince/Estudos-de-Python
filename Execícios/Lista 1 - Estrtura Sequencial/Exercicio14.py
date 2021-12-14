peso = float(input("Insira quantos Kg de peixe foi pescado: "))

if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print("O excesso foi: ", excesso, "Kg. O valor da multa e: R$", multa)

else: 
	print("A quantidade pescada nao excedeu o limite de 50Kg")

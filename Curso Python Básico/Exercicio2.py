##Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do exercito. Para entrar no exercito é preciso ter mais de 18 anos, pesar mais ou igual a 60kg e medir mais ou igual a 1,70 metros

idade = int(input("Insira a sua idade: "))
peso = float(input("Insira o seu peso: "))
altura = float(input("Insita a sua altura: "))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):

    print("Voce esta apto a entrar no exercito")

else:

    print("Voce nao esta apto a entrar no exercito")

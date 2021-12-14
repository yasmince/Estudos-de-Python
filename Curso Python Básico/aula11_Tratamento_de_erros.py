try:
    a = 1200 / 0
except ZeroDivisionError:
    print("Divisão por zero não é possível")
except NameError:
    print("Você digitou alguma coisa errada")
except Exception as erro:
    print("Aconteceu algum erro", erro)
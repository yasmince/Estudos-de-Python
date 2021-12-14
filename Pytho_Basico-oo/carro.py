from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo. __init__(self, cor, 4, marca, tanque)
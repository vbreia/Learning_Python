class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('\nLigando o motor ...')

    def __str__(self):
        return f"\n{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}\n"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(
            f"O caminhão {'ESTÁ' if self.carregado else '[NÃO] está'}  carregado\n")


moto = Motocicleta('preta', 'abc-1234', 2)
carro = Carro('Branco', 'xd2-0098', 4)
caminhao = Caminhao('Preto', 'lda-4431', 8, True)

print(caminhao)
caminhao.esta_carregado()
print(moto)
print(carro)

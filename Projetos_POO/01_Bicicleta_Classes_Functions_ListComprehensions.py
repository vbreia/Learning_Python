class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print('\nPlim, plim ... \n ')

    def parar(self):
        print('Parando biscicleta ...')
        print('Biscicleta parada. \n ')

    def correr(self):
        print('Vrummm ...\n')

    def __str__(self):
        return f"\n{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}\n"


b1 = Bicicleta('vermelha', 'caloi',  2022, 500)
b2 = Bicicleta('Verde', 'Monark', 2000, 189)
print(b2)
b2.correr()

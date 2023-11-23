# herança múltipla
# super construtor
# kwargs

class Animal:
    def __init__(self, nome, nro_patas):
        self.nome = nome
        self.nro_patas = nro_patas

    def __str__(self):
        return f"\n{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self,  cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self,  cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class andarMixin:  # Classe mixin
    def andar(self):
        return '\nAndando... '


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave, andarMixin):
    pass


gato = Gato(nome='Frajola', nro_patas=4, cor_pelo='Preto e branco')
print(gato)

ornitorrinco = Ornitorrinco(nome='Perry',
                            nro_patas=4, cor_pelo='verde água', cor_bico='laranja')
print(ornitorrinco)

# Imprimindo método mixin
print(ornitorrinco.andar())

#  (MRO) Ordem de resolução do método
print(f'\nMRO da classe Ornitorrinco: \n{Ornitorrinco.mro()}')

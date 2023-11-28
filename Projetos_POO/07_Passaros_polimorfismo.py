class Passaro:
    def voar(self):
        print("\nVoando ...")
        
class Pardal(Passaro):
    def voar(self):
        print("\nPardal pode voar!")
        
class Avestruz(Passaro):
    def voar(self):
        print("\nAvestruz não pode voar!" )
        
# FIXME: exemplo ruim do uso de herança para "ganhar" o método voar       
class Aviao(Passaro):
    def voar(self):
        print("\nAvião está decolando ...")
        
def plano_voo(obj):
    obj.voar()



plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())


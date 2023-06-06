from model.edificio import Edificio
class Quarto:
    def __init__(self):
        self._numero = 0
        self._andar = 0
        self._edificio = None
    
    def getNumero(self):
        return self._numero
    
    def setNumero(self, numero):
        self._numero = numero
    
    def getAndar(self):
        return self._andar
    
    def setAndar(self, andar):
        self._andar = andar
    
    def getEdificio(self):
        return self._edificio
    
    def setEdificio(self, edificio: Edificio):
        self._edificio = edificio
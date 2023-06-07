from model.endereco import Endereco

class Edificio:
    def __init__(self):
        self._nome = ''
        self._qtdAndares = 0
        self._qtdQuartos = 0
        self._endereco = None
    
    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome
    
    def getQtdAndares(self):
        return self._qtdAndares
    
    def setQtdAndares(self, qtdAndar):
        self._qtdAndares = qtdAndar
    
    def getQtdQuartos(self):
        return self._qtdQuartos
    
    def setQtdQuartos(self, qtdQuartos):
        self._qtdQuartos = qtdQuartos
    
    def getEndereco(self):
        return self._endereco
    
    def setEndereco(self, endereco: Endereco):
        self._endereco = endereco
        
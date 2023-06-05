
from datetime import date

class Hospede:
    def __init__(self):
        self._cliente = ""
        self._quarto = 0
        self._andar = 0
        self._edificio = 0
        self._dataEntrada = None
        self._dataVencimento = None
        self._dataSaida = None
    
    def getCliente(self):
        return self._cliente
    
    def setCliente(self, cliente):
        self._cliente = cliente
    
    def getQuarto(self):
        return self._quarto
    
    def setQuarto(self, quarto):
        self._quarto = quarto
    
    def getAndar(self):
        return self._andar
    
    def setAndar(self, andar):
        self._andar = andar
    
    def getEdificio(self):
        return self._edificio
    
    def setEdificio(self, edificio):
        self._edificio = edificio
    
    def getDataEntrada(self):
        return self._dataEntrada
    
    def setDataEntrada(self, ano, mes, dia):
        self._dataEntrada = date(ano, mes, dia)
    
    def getDataVencimento(self):
        return self._dataVencimento
    
    def setDataVencimento(self, ano, mes, dia):
        self._dataVencimento = date(ano, mes, dia)
        
    def getDataSaida(self):
        return self._dataSaida
    
    def setDataSaida(self, ano, mes, dia):
        self._dataSaida = date(ano, mes, dia)
        
    
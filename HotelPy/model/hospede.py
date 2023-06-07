from model.cliente import Cliente
from model.quarto import Quarto
from model.telefone import Telefone
from datetime import date

class Hospede:
    def __init__(self):
        self._cliente = ""
        self._telefoneCliente = None
        self._quarto = 0
        self._dataEntrada = None
        self._dataVencimento = None
        self._dataSaida = None
    
    def getCliente(self):
        return self._cliente
    
    def setCliente(self, cliente: Cliente):
        self._cliente = cliente
    
    def getTelefoneCliente(self):
        return self._telefoneCliente
    
    def setTelefoneCliente(self, telefoneCliente: Telefone):
        self._telefoneCliente = telefoneCliente
    
    def getQuarto(self):
        return self._quarto
    
    def setQuarto(self, quarto: Quarto):
        self._quarto = quarto
    
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
        
    
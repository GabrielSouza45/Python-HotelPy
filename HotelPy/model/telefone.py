from model.cliente import Cliente
class Telefone:
    def __init__(self):
        self.numero = ""
        self.cliente =  None
        self.edificio =  None
        
        
    def setNumero(self, numero):
        self.numero = numero
        
    def getNumero(self):
        return self.numero
        
    def setCliente(self, cliente: Cliente):
        self.cliente = cliente
        
    def getCliente(self):
        return self.cliente
        
    def setEdificio(self, edificio):
        self.edificio = edificio
    
    def getEdificio(self):
        return self.edificio
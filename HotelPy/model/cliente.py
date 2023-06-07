from model.endereco import Endereco

class Cliente: 
    def __init__(self):
        self._nome = ""
        self._cpf = ""
        self._email = ""
        self._endereco = None
        
    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome
    
    def getCpf(self):
        return self._cpf
    
    def setCpf(self, cpf):
        self._cpf = cpf
    
    def getEmail(self):
        return self._email
    
    def setEmail(self, email):
        self._email = email
    
    def getEndereco(self):
        return self._endereco
    
    def setEndereco(self, endereco: Endereco):
        self._endereco = endereco
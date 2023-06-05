class Cliente: 
    def __init__(self):
        self._nome = ""
        self._cpf = ""
        self._telefone = ""
        self._email = ""
        
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
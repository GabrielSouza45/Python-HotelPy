from service.clienteService import ClienteService

class ClienteController:
    def __init__(self) :
        self.service = ClienteService()
    
    def cadastrarCliente(self, nome, cpf, email, endereco):
        return self.service.cadastrarCliente(nome, cpf, email, endereco)
    

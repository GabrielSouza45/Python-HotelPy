from service.enderecoService import EnderecoService

class EnderecoController:
    def __init__(self):
        self.service = EnderecoService()
    
    def cadastrarEndereco(self, cep, rua, numero, bairro, cidade, estado):
        return self.service.cadastrarEndereco(cep, rua, numero, bairro, cidade, estado)
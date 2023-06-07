from service.telefoneService import TelefoneService
class TelefoneController():
    def __init__(self):
        self.service = TelefoneService()
    
    def cadastrarTelefone(self, numero, cliente, edificio):
        return self.service.cadastrarTelefone(numero, cliente, edificio)
        
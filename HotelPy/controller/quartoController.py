from service.quartoService import QuartoService
class QuartoController:
    def __init__(self):
        self.service = QuartoService()
    
    def cadastrarQuarto(self, numero, andar, edificio):
        return self.service.cadastrarQuarto(numero, andar, edificio)
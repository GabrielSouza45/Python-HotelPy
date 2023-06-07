from service.edificioService import EdificioService

class EdificioController:
    def __init__(self):
        self.service = EdificioService()
    
    def cadastrarEdificio(self, nome, qtdAndar, qtdQuartos, endereco):
        return self.service.cadastrarEdificio(nome, qtdAndar, qtdQuartos, endereco)
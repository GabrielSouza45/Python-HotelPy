from model.edificio import Edificio

class EdificioService:
    def cadastrarEdificio(self, nome, qtdQuartos, qtdAndar, endereco):
        edificio = Edificio()
        edificio.setNome(nome)
        edificio.setQtdQuartos(qtdQuartos)
        edificio.setQtdAndares(qtdAndar)
        edificio.setEndereco(endereco)
        
        return edificio
from model.quarto import Quarto

class QuartoService:
    def cadastrarQuarto(self, numero, andar, edificio):
        quarto = Quarto()
        quarto.setNumero(numero)
        quarto.setAndar(andar)
        quarto.setEdificio(edificio)
        
        return quarto

from service.hospedeService import HospedeService
class HospedeController:
    def __init__(self):
        self.service = HospedeService()
    
    def cadastrarHospede(self, cliente, telefoneCliente, quarto, dataEntrada, dataVencimento, dataSaida):
        return self.service.cadastrarHospede(cliente, telefoneCliente, quarto, dataEntrada, dataVencimento, dataSaida)
    
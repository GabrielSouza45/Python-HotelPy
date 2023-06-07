from model.hospede import Hospede

class HospedeService:
    def cadastrarHospede(self, cliente, telefoneCliente, quarto, dataEntrada, dataSaida, dataVencimento):
        hospede = Hospede()
        hospede.setCliente(cliente)
        hospede.setTelefoneCliente(telefoneCliente)
        hospede.setQuarto(quarto)
        hospede.setDataEntrada(dataEntrada)
        hospede.setDataSaida(dataSaida if dataSaida != None else None )
        hospede.setDataVencimento(dataVencimento)
        
        return hospede 
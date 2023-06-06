from model.telefone import Telefone

class TelefoneService:
    def cadastrarTelefone(self, numero, cliente, edificio):
        # sourcery skip: inline-immediately-returned-variable
        telefone = Telefone()
        telefone.setNumero(numero)
        telefone.setCliente(cliente if cliente != None else None)
        telefone.setEdificio(edificio if edificio != None else None)
        
        return telefone

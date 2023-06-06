from model.cliente import Cliente

class ClienteService:
    def cadastrarCliente(self, nome, cpf, email):
        # sourcery skip: inline-immediately-returned-variable
        cliente = Cliente()
        cliente.setNome(nome)
        cliente.setCpf(cpf)
        cliente.setEmail(email)
        
        return cliente
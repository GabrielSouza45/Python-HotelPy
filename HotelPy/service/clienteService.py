from model import cliente

def cadastrarCliente():
    cliente1 = cliente.Cliente()
    cliente1.setNome(input("Digite seu nome: "))
    cliente1.setEmail(input("Digite seu email: "))
    cliente1.setCpf(input("Digite seu CPF: "))
    return cliente1
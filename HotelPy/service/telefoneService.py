from model import *

def cadastrarTelefoneCliente(cliente):
    telefone1 = telefone.Telefone()
    telefone1.setCliente = cliente
    telefone1.setNumero = input("Digite seu telefone: ")
    return(telefone1)
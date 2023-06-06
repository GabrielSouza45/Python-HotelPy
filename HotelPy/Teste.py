from model import *
from service import *
from controller import *

def reservar(rsvEdfc, rsvAnd, rsvQat, quartosReservados, listaDeReservas):
    reservado = True

    hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] = reservado
    quartosReservados[1] = (rsvEdfc)
    quartosReservados[3] = (rsvAnd)
    quartosReservados[5] = (rsvQat)
    
    quarto_controller = quartoController.QuartoController()
    
    quarto = quarto_controller.cadastrarQuarto(rsvQat, rsvAnd, rsvEdfc)
    
    listaAuxiliar = quartosReservados[:]
    listaDeReservas.append(listaAuxiliar)
    return (quartosReservados, listaDeReservas)

def cadastraEndereco():
    endereco_controller = enderecoController.EnderecoController()
    endereco1 = endereco_controller.cadastrarEndereco(
        "589648557", "Rua da marinha", "165", "RedLine", "São Paulo", "SP")
    
    endereco2 = endereco_controller.cadastrarEndereco(
        "123456789", "Rua dos almirantes", "190", "Navio 56", "São Jorge", "SP")
    
    endereco3 = endereco_controller.cadastrarEndereco(
        "987654321", "Rua dos Chapéis de palha", "15b", "", "Thousand Sunny", "SP")
    return [endereco1, endereco2, endereco3]
    

def cadastraEdificio():
    end = cadastraEndereco()
    edificio_controller = edificioController.EdificioController()
    edificio1 = edificio_controller.cadastrarEdificio("MarineFord", 1, 5, end[0])
    edificio2 = edificio_controller.cadastrarEdificio("Roma", 2, 5, end[1])
    edificio3 = edificio_controller.cadastrarEdificio("One Piece", 3, 5, end[2])
    
    return [edificio1, edificio2, edificio3]


hotel = [[[ False for _ in range(5)] for _ in range(5)] for _ in range(3)] 
#print(hotel)
print()

nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
email = input("Digite seu email: ")
numero = input("Digite seu telefone: ")

cliente_service = clienteService.ClienteService()
telefone_service = telefoneService.TelefoneService()

cliente = cliente_service.cadastrarCliente(nome, cpf, email)
telefone = telefone_service.cadastrarTelefone(numero, cliente, None)

primeiroNome = cliente.getNome().split(None, 1)[0]

edificios = cadastraEdificio()
edificio1 = edificios[0]
edificio2 = edificios[1]
edificio3 = edificios[2]
print()

print("Edificio 1: ", edificio1.getNome())
print("Localizacao: ")
print("Rua: ", edificio1.getEndereco().getRua())
print("Cep: ", edificio1.getEndereco().getCep())
print()

print("Edificio 2: ", edificio2.getNome())
print("Localizacao: ")
print("Rua: ", edificio2.getEndereco().getRua())
print("Cep: ", edificio2.getEndereco().getCep())
print()

print("Edificio 3: ", edificio3.getNome())
print("Localizacao: ")
print("Rua: ", edificio3.getEndereco().getRua())
print("Cep: ", edificio3.getEndereco().getCep())
print()

qtdReservar = int(input("Olá {nome}, quantos quartos deseja reservar hoje? ".format(nome = primeiroNome)))


quartosReservados = ["Edifício:", 0, "Andar:", 0, "Quarto:", 0]
listaDeReservas = []
reservados = 0
totalQuartos = len(hotel) * len(hotel[0]) * len(hotel[0][0])
quartosDisponiveis = 0
loop = 0

print() 
while loop < qtdReservar:
    quartosDisponiveis = totalQuartos - reservados 
    print()
    print("Quartos já reservados: ", reservados)
    print("Quartos disponíveis: ", quartosDisponiveis)
    print()
    rsvEdfc = int(input("Em qual edifício gostaria de alugar o quarto? \n (1 à {edificio}): ".format(edificio=len(hotel))))
    rsvAnd  = int(input("Em qual andar gostaria de alugar o quarto? \n (1 à {andar}): ".format(andar=len(hotel[0]))))
    rsvQat  = int(input("Em qual quarto gostaria de se alojar? \n (1 à {quarto}): ".format(quarto=len(hotel[0][0]))))

    if hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] == True :
        print("Desculpe, este quarto não está disponível no momento, tente algum outro.")
        continue
    
    reservar(rsvEdfc, rsvAnd, rsvQat, quartosReservados, listaDeReservas)
    reservados += 1
    loop+=1

print()
print("Quartos reservados: ")
for i in listaDeReservas:
    print(i)



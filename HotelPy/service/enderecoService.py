from model.endereco import Endereco

class EnderecoService:
    def cadastrarEndereco(self, cep, rua, numero, bairro, cidade, estado):
        endereco = Endereco()
        endereco.setCep(cep)
        endereco.setRua(rua)
        endereco.setNumero(numero)
        endereco.setBairro(bairro)
        endereco.setCidade(cidade)
        endereco.setEstado(estado)
        
        return endereco
        
        
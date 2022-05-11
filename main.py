# #Validação e formatação de CPF e CNPJ
# from cpf_cnpj import Documento
#
# try:
#     exemplo = '92102424000111'
#     doc = Documento.cria_documento(exemplo)
#     print(doc)
# except Exception as error:
#     print(error)

# #Validação e formatação de telefones
# try:
#     from TelefonesBr import TelefonesBr
#     telefone = "45fff000 556133394046"
#     telefone_objeto = TelefonesBr(telefone)
#     print(telefone_objeto)
# except Exception as error:
#     print(error)

# #Validação e formatação de datas
# from DatasBr import DatasBr
#
# cadastro_usuario = DatasBr()
#
# print(cadastro_usuario.momento_cadastro)
# print(cadastro_usuario.mes_cadastro())
# print(cadastro_usuario.dia_semana_cadastro())
# print(cadastro_usuario)
#
# print(cadastro_usuario.tempo_de_cadastro())

from acesso_cep import BuscaEndereco

cep = 71694018
cep_objeto = BuscaEndereco(cep)
bairro, localidade, uf = cep_objeto.acessa_via_cep()
print(bairro, localidade, uf)

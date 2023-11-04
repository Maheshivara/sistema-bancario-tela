import validate_docbr
from ..classes import usuario as cl

def logar():

  cpf_validator = validate_docbr.CPF()
  cpf = input("Digite seu cpf no formato NNN.NNN.NNN-NN: ")
  checar_cpf = cpf_validator.validate(cpf)

  if(not checar_cpf):
    print("CPF inválido, por favor tente novamente")
    return
  
  senha = input("Digite sua senha: ")

  if(len(senha<8)):
    print("Senha incorreta")
    return
  
  if(senha == "temporario"):
    usuario = cl.Usuario(cpf,cl.nc.Numero_conta,"teste@mail.com",senha,"Fulano de Tal",82000000000,0,[])
    print(usuario)


  
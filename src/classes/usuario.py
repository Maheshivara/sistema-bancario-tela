import typing
import bcrypt
import numero_conta as nc
import transacao as tr

class Usuario:
  def __init__(self,cpf:int,numero_conta:nc.Numero_conta,email:str,senha:str,nome:str,telefone:int,saldo:float,extrato:typing.List[tr.Transacao]) -> None:
    self.cpf = cpf
    self.numero_conta = numero_conta
    self.email = email
    self.senha = senha
    self.nome = nome
    self.telefone = telefone
    self.saldo = saldo
    self.extrato = extrato

def login(self,senha:str) -> bool:
  """
  Compara a senha informada com a senha do usuário

  Args:
      senha (str): Senha para comparar

  Returns:
      bool: True para senha correta, False para senha incorreta
  """
  return bcrypt.checkpw(bytes(senha),self.senha)
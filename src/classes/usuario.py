import typing
import bcrypt
import datetime
import numero_conta as nc
import transacao as tr

class Usuario:
  def __init__(self,cpf:str,numero_conta:nc.Numero_conta,email:str,senha:str,nome:str,telefone:int,saldo:float,extrato:typing.List[tr.Transacao]) -> None:
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
  
  def sacar(self,valor:float)->bool:
    """
    Remove do saldo o valor sacado e adiciona a transação ao extrato

    Args:
        valor (float): Valor a ser retirado

    Returns:
        bool: True caso a transação seja efetuada, False caso não seja efetuada
    """

    if (valor>self.saldo or valor<0):
      return False
    
    self.saldo -= valor
    self.extrato.append(tr.Transacao("Saque",datetime.datetime.now(),valor,self.nome))

    return True
  
  def depositar(self,valor:float)->bool:
    """
    Adiciona ao saldo o valor sacado e adiciona a transação ao extrato

    Args:
        valor (float): Valor a ser adicionado

    Returns:
        bool: True caso a transação seja efetuada, False caso não seja efetuada
    """

    if (valor<0):
      return False
    
    self.saldo += valor
    self.extrato.append(tr.Transacao("Deposito",datetime.datetime.now(),valor,self.nome))

    return True
    
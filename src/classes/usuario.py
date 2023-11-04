import typing
import bcrypt
import datetime
from src.classes.numero_conta import Numero_conta
from src.classes.transacao import Transacao

class Usuario:
  def __init__(self,cpf:str,numero_conta:Numero_conta,email:str,senha_hash:bytes,nome:str,telefone:int,saldo:float,extrato:typing.List[Transacao]) -> None:
    self.cpf = cpf
    self.numero_conta = numero_conta
    self.email = email
    self.senha_hash = senha_hash
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
    return bcrypt.checkpw(senha.encode("utf-8"),self.senha_hash)
  
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
    self.extrato.append(Transacao("Saque",datetime.datetime.now(),valor,self.nome))

    return True
  
  def depositar(self,valor:float)->bool:
    """
    Adiciona ao saldo o valor depositado e adiciona a transação ao extrato

    Args:
        valor (float): Valor a ser adicionado

    Returns:
        bool: True caso a transação seja efetuada, False caso não seja efetuada
    """

    if (valor<0):
      return False
    
    self.saldo += valor
    self.extrato.append(Transacao("Deposito",datetime.datetime.now(),valor,self.nome))

    return True
  
  def pagamento(self,codigo:int,valor:float)->bool:
    """
    Remove o valor da conta e adiciona a transação ao extrato

    Args:
        valor (float): Valor a ser removido

    Returns:
        bool: True caso a transação seja efetuada, False caso não seja efetuada
    """

    if (valor<0 or valor>self.saldo):
      return False
    
    self.saldo -= valor
    self.extrato.append(Transacao("Pagamento",datetime.datetime.now(),valor,codigo))

    return True
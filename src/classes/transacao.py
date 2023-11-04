import datetime
class Transacao:
  def __init__(self,tipo:str,data:datetime.datetime,valor:float,destino:str) -> None:
    self.tipo = tipo
    self.data = data
    self.valor = valor
    self.destino = destino
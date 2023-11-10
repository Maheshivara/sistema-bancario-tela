import datetime


class Transacao:
    def __init__(
        self, tipo: str, data: datetime.datetime, valor: float, destino: str
    ) -> None:
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.destino = destino

    def print(self):
        """
        Exibe no terminal de forma legivel as informações da transação
        """
        print(
            f'Data: {str(self.data)}, Tipo: {self.tipo}, Valor: {self.valor:.2f}, Destino: {self.destino}'
        )

    def salvar(self) -> dict:
        """
        Auxilio para salvar o arquivo

        Return:
            Dicionário da transação
        """
        return {
            'data': str(self.data),
            'tipo': self.tipo,
            'valor': self.valor,
            'destino': self.destino,
        }

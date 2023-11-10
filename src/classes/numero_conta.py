class Numero_conta:
    def __init__(self, agencia: int, numero: int) -> None:
        self.agencia = agencia
        self.numero = numero

    def print(self) -> None:
        """
        Exibe no terminal a agencia e numero da conta
        """

        print(f'Agencia: {self.agencia}\nConta: {self.numero}')

    def salvar(self) -> dict:
        """
        Auxilio para salvar o arquivo
        """
        return {'agencia': self.agencia, 'numero': self.numero}

import typing
import bcrypt
import datetime
import re
from src.classes.numero_conta import Numero_conta
from src.classes.transacao import Transacao


class Usuario:
    def __init__(
        self,
        cpf: str,
        numero_conta: Numero_conta,
        email: str,
        senha_hash: bytes,
        nome: str,
        telefone: int,
        saldo: float,
        extrato: typing.List[Transacao],
    ) -> None:
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.email = email
        self.senha_hash = senha_hash
        self.nome = nome
        self.telefone = telefone
        self.saldo = saldo
        self.extrato = extrato

    def login(self, senha: str) -> bool:
        """
        Compara a senha informada com a senha do usuário

        Args:
            senha (str): Senha para comparar

        Returns:
            bool: True para senha correta, False para senha incorreta
        """
        check = bcrypt.checkpw(senha.encode('utf-8'), self.senha_hash)
        return check

    def sacar(self, valor: float) -> bool:
        """
        Remove do saldo o valor sacado e adiciona a transação ao extrato

        Args:
            valor (float): Valor a ser retirado

        Returns:
            bool: True caso a transação seja efetuada, False caso não seja efetuada
        """

        if valor > self.saldo or valor < 0:
            return False

        self.saldo -= valor
        self.extrato.append(
            Transacao('Saque', datetime.datetime.now(), valor, self.nome)
        )

        return True

    def depositar(self, valor: float) -> bool:
        """
        Adiciona ao saldo o valor depositado e adiciona a transação ao extrato

        Args:
            valor (float): Valor a ser adicionado

        Returns:
            bool: True caso a transação seja efetuada, False caso não seja efetuada
        """

        if valor < 0:
            return False

        self.saldo += valor
        self.extrato.append(
            Transacao('Deposito', datetime.datetime.now(), valor, self.nome)
        )

        return True

    def pagamento(self, codigo: int, valor: float) -> bool:
        """
        Remove o valor da conta e adiciona a transação ao extrato

        Args:
            valor (float): Valor a ser removido

        Returns:
            bool: True caso a transação seja efetuada, False caso não seja efetuada
        """

        if valor < 0 or valor > self.saldo:
            return False

        self.saldo -= valor
        self.extrato.append(
            Transacao('Pagamento', datetime.datetime.now(), valor, codigo)
        )

        return True

    def atualizar_email(self) -> None:
        """
        Pede, via terminal, um novo email e atualiza no usuário
        """

        while True:
            novo_email = input('Digite o seu novo email:\n')
            # Traduzindo o regex: Ao menos um caractere diferente de '@' + um '@' + Ao menos um caractere diferente de '@' + um '.' + Algum(s) caractere
            if re.match(r'[^@]+@[^@]+\.[^@]+', email):
                break
            print('Email inválido')

        self.email = novo_email
        return

    def atualizar_senha(self) -> None:
        """
        Pede, via terminal, uma nova senha e atualiza no usuário
        """

        while True:
            nova_senha = input('Digite a senha para o novo usuário:\n')
            if len(senha) >= 8:
                break
            print('A senha deve possuir ao menos 8 caracteres')

        salt = bcrypt.gensalt()
        nova_senha_hash = bcrypt.hashpw(nova_senha.encode('utf-8'), salt)

        self.senha_hash = nova_senha_hash
        return

    def atualizar_telefone(self):
        """
        Pede, via terminal, um novo telefone e atualiza no usuário
        """

        while True:
            telefone = input('Digite seu novo telefone:\n')
            if telefone.isdigit():
                telefone = int(telefone)
                break
            print('Telefone inválido, use apenas números')

        self.telefone = telefone
        return

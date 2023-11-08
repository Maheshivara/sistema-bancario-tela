import bcrypt
import typing
import re
import validate_docbr
import os
from src.classes.usuario import Usuario
from src.classes.numero_conta import Numero_conta


def criar_usuario(usuarios: typing.List[Usuario]) -> typing.Union[Usuario, None]:
    """
    Solicita os dados para a criação de um usuário

    Returns:
        Usuario: O objeto usuário com as informações passadas
    """

    cpf_validator = validate_docbr.CPF()
    while True:
        cpf = input('Digite o CPF do novo usuário (apenas números):\n')
        if cpf.isdecimal() and cpf_validator.validate(cpf):
            break
        print('CPF inválido, tente novamente')

    for usuario in usuarios:
        if cpf == usuario.cpf:
            print('CPF já cadastrado')
            return None

    while True:
        senha = input('Digite a senha para o novo usuário:\n')
        if len(senha) >= 8:
            break
        print('A senha deve possuir ao menos 8 caracteres')

    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

    while True:
        email = input('Digite o email do novo usuário:\n')
        # Traduzindo o regex: Ao menos um caractere diferente de '@' + um '@' + Ao menos um caractere diferente de '@' + um '.' + Algum(s) caractere
        if re.match(r'[^@]+@[^@]+\.[^@]+', email):
            break
        print('Email inválido')

    nome = input('Digite o nome do novo usuário:\n')

    while True:
        telefone = input('Insira o telefone do novo usuário:\n')
        if telefone.isdecimal() and len(telefone) == 11:
            telefone = int(telefone)
            break
        print('Numero de celular invalido!')

    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
    agencia = 123
    # Gerando um número de ao menos 7 digitos
    conta = (10**6) + len(usuarios) + 1

    numero_conta = Numero_conta(agencia, conta)
    novo_usuario = Usuario(cpf, numero_conta, email, senha_hash, nome, telefone, 0, [])

    return novo_usuario

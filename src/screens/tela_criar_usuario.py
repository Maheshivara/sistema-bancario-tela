import bcrypt
import typing
import validate_docbr
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

    email = input('Digite o email do novo usuário:\n')
    nome = input('Digite o nome do novo usuário:\n')
    telefone = int(input('Insira o telefone do novo usuário:\n'))

    agencia = 123
    conta = (10**35) + len(usuarios) + 1

    numero_conta = Numero_conta(agencia, conta)
    novo_usuario = Usuario(cpf, numero_conta, email, senha_hash, nome, telefone, 0, [])

    return novo_usuario

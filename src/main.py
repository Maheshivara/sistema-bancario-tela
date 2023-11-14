import os
import typing
import json
import simplejson
from datetime import datetime
from src.screens.tela_login import logar
from src.screens.tela_criar_usuario import criar_usuario
from src.classes.usuario import Usuario
from src.classes.numero_conta import Numero_conta
from src.classes.transacao import Transacao


def carregar_usuarios() -> typing.List[Usuario]:
    """
    Verifica a existência de dados no arquivo dados_usuario.json,
    e caso haja irá retornar os dados queridos.

    Returns:
        Lista de objetos usuário com as informações encontradas
    """

    def carregar_conta(dicionario: dict):
        return Numero_conta(dicionario.get('agencia'), dicionario.get('numero'))

    def carregar_extrato(dicionario_list: list):
        formato_str = '%Y-%m-%d %H:%M:%S.%f'
        return [
            Transacao(
                parte.get('tipo'),
                datetime.strptime(parte.get('data'), formato_str),
                parte.get('valor'),
                parte.get('destino'),
            )
            for parte in dicionario_list
        ]

    usuarios_list = []
    try:
        with open(file='dados_usuario.json', mode='r', encoding='utf8') as file:
            data = json.load(file)
            for user_data in data:
                user = Usuario(
                    user_data['cpf'],
                    carregar_conta(user_data['numero_conta']),
                    user_data['email'],
                    user_data['senha_hash'].encode('utf-8'),
                    user_data['nome'],
                    user_data['telefone'],
                    user_data['saldo'],
                    carregar_extrato(user_data['extrato']),
                )
                usuarios_list.append(user)
    except FileNotFoundError:
        pass
    return usuarios_list


def salvar_usuarios(usuarios: typing.List[Usuario]) -> None:
    """
    Salva os dados dos usuarios em arquivo dados_usuario.json

    Args:
        usuarios: a lista de objeto usuário com as informações passadas
    """
    with open(file='dados_usuario.json', mode='w', encoding='utf8') as file:
        dados = [
            {
                'cpf': user.cpf,
                'numero_conta': user.numero_conta.salvar(),
                'email': user.email,
                'senha_hash': user.senha_hash.decode('utf-8'),
                'nome': user.nome,
                'telefone': user.telefone,
                'saldo': user.saldo,
                'extrato': [i.salvar() for i in user.extrato],
            }
            for user in usuarios
        ]
        simplejson.dump(dados, file, sort_keys=True, indent=4 * ' ')


if __name__ == '__main__':
    running = True
    usuarios = carregar_usuarios()
    while running:
        print('Olá, você pode:\n 1- Cadastrar Usuário\n 2- Realizar Login\n 3- Sair')
        opc = input('Digite a opção desejada: ')
        if not opc.isnumeric():
            print('Opção inválida')
            continue
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
        opc = int(opc)
        match opc:
            case 1:
                novo_usuario = criar_usuario(usuarios)
                if not novo_usuario is None:
                    usuarios.append(novo_usuario)
                    print('Sua nova conta é:')
                    novo_usuario.numero_conta.print()

            case 2:
                logar(usuarios)
            case 3:
                print('Obrigado e até a próxima')
                salvar_usuarios(usuarios=usuarios)
                running = False
            case _:
                print('Opção inválida')

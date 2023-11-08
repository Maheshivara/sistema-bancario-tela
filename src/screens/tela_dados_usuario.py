from os import system
from src.classes.usuario import Usuario


def mostrar_tela_dados(usuario: Usuario) -> None:
    system('cls')
    print(
        'Você pode:\n 1 - Mudar email\n 2 - Mudar telefone\n 3 - Mudar senha\n 4 - Ver seus dados\n Outro - Voltar'
    )
    opc = input('O que você deseja fazer?\n')
    if not opc.isnumeric():
        print('Opção inválida')
        return
    opc = int(opc)
    match opc:
        case 1:
            usuario.atualizar_email()
        case 2:
            usuario.atualizar_telefone()
        case 3:
            usuario.atualizar_senha()
        case 4:
            print(f'\nCPF: {usuario.cpf}')
            print(f'Nome: {usuario.nome}')
            print(f'Email: {usuario.email}')
            print(f'Telefone: {usuario.telefone}')
            usuario.numero_conta.print()
        case _:
            print('Voltando...')
    return

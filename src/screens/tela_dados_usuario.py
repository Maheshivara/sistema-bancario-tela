from src.classes.usuario import Usuario


def mostrar_tela_dados(usuario: Usuario) -> None:
    print(
        'Você pode:\n 1 - Mudar email\n 2 - Mudar telefone\n 3 - Mudar senha\n 4- Ver seus dados\n Outro - Voltar'
    )
    opt = input('O que você deseja fazer?\n')
    if not opt.isnumeric():
        print('Opção inválida')
        return
    match opt:
        case 1:
            usuario.atualizar_email()
        case 2:
            usuario.atualizar_telefone()
        case 3:
            usuario.atualizar_senha()
        case 4:
            print(f'CPF: {usuario.cpf}')
            print(f'Nome: {usuario.nome}')
            print(f'Email: {usuario.email}')
            print(f'Telefone: {usuario.telefone}')
            print(
                f'Conta:\n Agencia: {usuario.numero_conta.agencia}\n Numero: {usuario.numero_conta.numero}\n'
            )
        case _:
            print('Voltando...')
    return

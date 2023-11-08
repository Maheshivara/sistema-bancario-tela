import typing
from src.classes.usuario import Usuario
from src.screens.tela_dados_usuario import mostrar_tela_dados


def logar(usuarios: typing.List[Usuario]):

    cpf = input('Digite seu cpf (somente números): ')
    if not cpf.isdecimal() or len(cpf) != 11:
        print('Formato inválido')
        return

    for usuario in usuarios:
        if usuario.cpf == cpf:
            senha = input('Digite sua senha: ')
            if usuario.login(senha):
                mostrar_tela_usuario(usuario)
            else:
                print('Senha incorreta')
            return

    print('Usuario não cadastrado')
    return


def mostrar_tela_usuario(usuario: Usuario):

    logado = True

    while logado:
        print(f'Olá {usuario.nome}')
        print(
            'Operações:\n 1- Saque\n 2- Deposito\n 3- Transferência\n 4- Pagamento\n 5- Ver Saldo\n 6- Ver Extrato\n 7- Ver dados\n 8- Sair'
        )

        opc = input('Qual operação voce deseja realizar hoje?\n')
        if not opc.isnumeric():
            print('Opção inválida')
            continue

        opc = int(opc)
        match opc:
            case 1:
                while True:
                    try:
                        valor = float(input('Quanto você deseja depositar?\n'))
                    except ValueError:
                        print('Erro de digitação, por favor digite novamente')
                    else:
                        break
                resultado = usuario.sacar(valor)
                print('Operação efetuada com sucesso') if resultado else print(
                    'Não foi possível realizar a transação'
                )

            case 2:
                while True:
                    try:
                        valor = float(input('Quanto você deseja depositar?\n'))
                    except ValueError:
                        print('Erro de digitação, por favor digite novamente')
                    else:
                        break
                resultado = usuario.depositar(valor)
                print('Operação efetuada com sucesso') if resultado else print(
                    'Não foi possível realizar a transação'
                )

            case 3:
                print('A implementar')

            case 4:
                while True:
                    try:
                        codigo = int(input('Digite o código do boleto:\n'))
                    except ValueError:
                        print('Erro de digitação, por favor digite novamente')
                    else:
                        break
                while True:
                    try:
                        valor = float(input('Qual valor do boleto?\n'))
                    except ValueError:
                        print('Erro de digitação, por favor digite novamente')
                    else:
                        if valor < 0:
                            print('Valor negativo!')
                        else:
                            break
                resultado = usuario.pagamento(codigo, valor)
                print('Operação efetuada com sucesso') if resultado else print(
                    'Não foi possível realizar a transação'
                )

            case 5:
                print(f'Seu saldo é de {usuario.saldo:.2f} reais')

            case 6:
                for transacao in usuario.extrato:
                    transacao.print()

            case 7:
                mostrar_tela_dados(usuario)

            case 8:
                logado = False

            case _:
                print('Operação inválida')

from src.screens.tela_login import logar
from src.screens.tela_criar_usuario import criar_usuario

if __name__ == '__main__':
    running = True
    usuarios = []
    while running:
        print('Olá, você pode:\n 1- Cadastrar Usuário\n 2- Realizar Login\n 3- Sair')
        opc = input('Digite a opção desejada: ')
        if not opc.isnumeric():
            print('Opção inválida')
            continue

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
                running = False
            case _:
                print('Opção inválida')

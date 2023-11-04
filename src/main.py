from src.screens.tela_login import logar

if __name__ == "__main__":
  running = True
  while(running):
    print("Olá, você pode:\n 1- Cadastrar Usuário\n 2- Realizar Login\n 3- Sair")

    try:
      opt = int(input("Digite a opção desejada: "))
    except:
      print("Opa, a opção escolhida não parece válida, por favor tente novamente, caso acredite que isso seja um erro contate o administrador")
      continue

    match opt:
      case 1:
        print("Substituto temporário para tela de cadastro de usuário")
      case 2:
        logar()
      case 3:
        print("Obrigado e até a próxima")
        running = False
      case _:
        print("Opção inválida")
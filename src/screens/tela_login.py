import typing
from src.classes.usuario import Usuario
from src.classes.numero_conta import Numero_conta

def logar(usuarios:typing.List[Usuario]):

  cpf = input("Digite seu cpf (somente números): ")
  if not cpf.isdecimal():
    print("Formato inválido")
    return

  for usuario in usuarios:
    if usuario.cpf == cpf:
      senha = input("Digite sua senha: ")
      if usuario.login(senha):
        mostrar_tela_usuario(usuario)
      else:
        print("Senha incorreta")
      return
  
  print("Usuario não cadastrado")
  return

def mostrar_tela_usuario(usuario:Usuario):

  logado = True

  while(logado):
    print(f'Olá {usuario.nome}')
    print("Operações:\n 1- Saque\n 2- Deposito\n 3- Transferencia\n 4- Pagamento\n 5- Ver Saldo\n 6- Ver Extrato\n 7- Sair")

    try:
      opc = int(input("Qual operação voce deseja realizar hoje?\n"))
    except:
      print("Opa, essa operação parece inválida, caso acredite que essa mensagem seja um erro contate o administrador")
      continue
    
    match opc:
      case 1:
        valor = float(input("Quanto você deseja sacar?\n"))
        resultado = usuario.sacar(valor)
        print("Operação efetuada com sucesso") if resultado else print("Não foi possivel realizar a transação")
        
      case 2:
        valor = float(input("Quanto você deseja depositar?\n"))
        resultado = usuario.depositar(valor)
        print("Operação efetuada com sucesso") if resultado else print("Não foi possivel realizar a transação")
      
      case 3:
        print("A implementar")
      
      case 4:
        codigo = int(input("Digite o codigo do boleto:\n"))
        valor = float(input("Qual valor do boleto?\n"))
        resultado = usuario.pagamento(codigo,valor)
        print("Operação efetuada com sucesso") if resultado else print("Não foi possivel realizar a transação")

      case 5:
        print(f'Seu saldo é de {usuario.saldo:.2f} reais')
      
      case 6:
        for transacao in usuario.extrato:
          transacao.print()

      case 7:
        logado = False

      case _:
        print("Operação inválida")
usuario = {}
logado = False

def cadastro():
  global usuario
  
  if usuario:
    print("Desculpe, mas já existe um cadastro. ")
    
  else:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    usuario['nome'] = nome
    usuario['senha'] = senha
    print(f"Nome: {nome}, Senha: {senha}.") 
    print("Cadastro realizado!")
    
def login():
  global logado
  
  if not usuario:
    print("Nenhum cadastro encontrado. ")
    return
  
  name = input("Digite o nome do usuário: ")
  password = input("Digite sua senha: ")
  
  if name == usuario.get('nome') and password == usuario.get('senha'):
    logado = True
    print("Login realizado!")
    
  else:
    print("Dados inválidos.")
    
def alterar_senha():
  global usuario
  global logado
  
  if not logado:
    print("É preciso estar logado para realizar a alteração de senha.")
    return
  
  senha_atual = input("Digite a senha: ")

  if senha_atual == usuario.get('senha'):
      nova_senha = input("Digite a nova senha: ")
      usuario['senha'] = nova_senha
      print("Sua senha foi alterada!")
  
  else:
      print("Senha atual inválida.")
  
def logout():
  
  global logado
  if logado:
    logado = False
    print("Pronto! Logout realizado!")
  
  else:
    print("Você não está logado.")
    
def menu():
  while True:
    
    print("\n===== MENU =====")
    print("-" * 30)
    
    print("Passo 1 - Cadastro")
    print("Passo 2 - Login")
    print("Passo 3 - Alteração de senha")
    print("Passo 4 - Logout (sair)")
    print("Passo 5 - Sair")
    
    opcao = input("Escolha uma dessas opções: ")
    
    if opcao == "1":
      cadastro()
      
    elif opcao == "2":
      login()
      
    elif opcao == "3":
      alterar_senha()
      
    elif opcao == "4":
      logout()
      
    elif opcao == "5":
      print("Saindo...")
      break
    
    else:
      print("Inválido.")
      
menu()

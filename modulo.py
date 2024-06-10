from datetime import date

# função exibir o menu
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{'#' * 20} PyBank | {dia}/{mes}/{ano} {'#' * 20}\n')
    print("1. Cadastrar usuário.")
    print("2. Deletar usuário.")
    print("3. Consultar saldo.")
    print("4. Depositar.")
    print("5. Sacar.")
    print("6. Sair.")


# Função para cadastrar um usuário
def cadastrar_usuario(usuarios):
    nome = input("Digite o nome a ser cadastrado: ")
    usuarios.append({"Nome": nome, "Saldo": 0.0})

# Função para deletar um usuário
def deletar_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja deletar: ")
    for usuario in usuarios:
        if usuario["Nome"] == nome:
            usuarios.remove(usuario)
            print(f"{nome} removido com sucesso.")
            break
    else:
        print(f"{nome} não encontrado.")

# Função para consultar saldo
def consultar_saldo(usuarios):
    nome = input("Digite o nome do usuário: ")
    for usuario in usuarios:
        if usuario["Nome"] == nome:
            print(f"Saldo de {nome}: R$ {usuario['Saldo']:.2f}")
            break
    else:
        print(f"{nome} não encontrado.")

# Função para depositar valor
def depositar(usuarios):
    nome = input("Digite o nome do usuário: ")
    for usuario in usuarios:
        if usuario["Nome"] == nome:
            valor = float(input("Digite o valor a ser depositado: "))
            usuario["Saldo"] += valor
            print(f"Depósito realizado! Novo saldo de {nome}: R$ {usuario['Saldo']:.2f}")
            break
    else:
        print(f"{nome} não encontrado.")

# Função para sacar valor
def sacar(usuarios):
    nome = input("Digite o nome do usuário: ")
    for usuario in usuarios:
        if usuario["Nome"] == nome:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor > usuario["Saldo"]:
                print("Saldo insuficiente.")
            else:
                usuario["Saldo"] -= valor
                print(f"Saque realizado! Novo saldo de {nome}: R$ {usuario['Saldo']:.2f}")
            break
    else:
        print(f"{nome} não encontrado.")

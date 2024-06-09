import os
from modulo import *


if __name__ == "__main__":
# Lista de dicionários para armazenar os usuários
    usuarios = []  

    while True:
        
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        os.system('cls')

        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            deletar_usuario(usuarios)
        elif opcao == '3':
            consultar_saldo(usuarios)
        elif opcao == '4':
            depositar(usuarios)
        elif opcao == '5':
            sacar(usuarios)
        elif opcao == '6':
            print("Obrigado por usar nosso aplicativo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


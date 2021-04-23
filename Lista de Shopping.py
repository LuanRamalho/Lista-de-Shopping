import sys

# Crie o menu principal
def mainMenu():
    while True:
        print()
        print('''### Lista de Compras ###

        Selecione um número para a ação que você gostaria de fazer:

        1. Ver lista de compras
        2. Adicionar item à lista de compras
        3. Remover item da lista de compras
        4. Verifique se o item está na lista de compras
        5. Quantos itens na lista de compras
        6. Limpar lista de compras
        7. Sair
        ''')

        selection = input("Faça sua seleção: ") # Peça ao usuário para fazer uma seleção

        # Determine qual ação executar com base na seleção do usuário
        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearList()
        elif selection == "7":
            sys.exit()
        else:
            print("Você não fez uma seleção válida.")

shopping_list = ["Maças", "Bananas", "Cenouras", "Batatas"] # Adicione alguns itens à lista de compras

# Exibe todos os itens da lista de compras
def displayList():
    print()
    print("--- LISTA DE COMPRAS ---")
    for i in shopping_list:
        print("* " + i)

# Adiciona um item à lista de compras
def addItem():
    item = input("Insira o item que deseja adicionar à lista de compras: ")
    shopping_list.append(item)
    print(item + " foi adicionado à lista de compras.")

# Remova um item da lista de compras
def removeItem():
    item = input("Insira o item que deseja remover da lista de compras: ")
    shopping_list.remove(item)
    print(item + " foi removido da lista de compras.")

# Verifique se um determinado item está na lista de compras
def checkItem():
    item = input("Qual item você gostaria de verificar na lista de compras: ")
    if item in shopping_list:
        print("Sim, " + item + " está na lista de compras.")
    else:
        print("Não, " + item + " não está na lista de compras.")

# Quantos itens estão na lista de compras
def listLength():
    print("Existem", len(shopping_list), "itens na lista de compras.")

# Remova tudo da lista de compras
def clearList():
    shopping_list.clear()
    print("A lista de compras agora está vazia.")

# Execute a função Menu principal que irá executar nosso aplicativo
mainMenu()
#MENU JOGO DE DAMA
opcao_menu = None
nome_jogador1 = ""
nome_jogador2 = ""
qtd_vitorias1 = 0
qtd_vitorias2 = 0
empates = 0

while opcao_menu != "4":
    print("==============================")
    print("Bem-vindo ao Jogo de Dama!")
    print("==============================")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Placar")
    print("4 - Sair")
    opcao_menu = input("Escolha uma opção: ")
    if opcao_menu == "1":
        print("Digite o nome dos jogadores:")
        nome_jogador1 = input("Jogador 1: ")
        nome_jogador2 = input("Jogador 2: ")
        print(f"Seja bem-vindo(a) {nome_jogador1} e {nome_jogador2}!")
        print("Iniciando o jogo de dama...")
        print("==============================")
        print("JOGO EM DESENVOLVIMENTO.....")
        print("==============================")
        resultado = int(input("Digite o resultado do jogo (1 para Jogador 1, 2 para Jogador 2, 3 para empate): "))
        if resultado == 1:
            qtd_vitorias1 += 1
            print(f"Jogador {nome_jogador1} venceu!")
        elif resultado == 2:
            qtd_vitorias2 += 1
            print(f"Jogador {nome_jogador2} venceu!")
        elif resultado == 3:
            empates += 1
            print("Empate!")
        else:
            print("Resultado inválido.")
    elif opcao_menu == "2":
        print("==============================")
        print("REGRAS EM DESENVOLVIMENTO.....")
        print("==============================")

    elif opcao_menu == "3":
        print("==============================")
        print("Placar:")
        if nome_jogador1 == "":
            print(f"Jogador 1: {qtd_vitorias1} vitórias")
        else:
            if qtd_vitorias1 == 1:
                print(f"{nome_jogador1}: {qtd_vitorias1} vitória")
            else:
                print(f"{nome_jogador1}: {qtd_vitorias1} vitórias")
        if nome_jogador2 == "":
            print(f"Jogador 2: {qtd_vitorias2} vitórias")
        else:
            if qtd_vitorias2 == 1:
                print(f"{nome_jogador2}: {qtd_vitorias2} vitória")
            else:
                print(f"{nome_jogador2}: {qtd_vitorias2} vitórias")
        print(f"Empates: {empates}")
        print("==============================")
    
    elif opcao_menu != "4":
        print("Opção inválida. Selecione uma opção novamente.")

print("Saindo do jogo. Até a próxima!")
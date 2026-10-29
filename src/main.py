#MENU JOGO DE DAMA
opcao = None
jogador_1 = ""
jogador_2 = ""
vitoria_1 = 0
vitoria_2 = 0
empates = 0

while opcao != "4":
    print("==============================")
    print("Bem-vindo ao Jogo de Dama!")
    print("==============================")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Placar")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("Digite o nome do Jogador 1:")
        jogador_1 = input("Jogador 1: ")
        print("Digite o nome do Jogador 2:")
        jogador_2 = input("Jogador 2: ")
        print("Iniciando o jogo de dama...")
        print("==============================")
        print("JOGO EM DESENVOLVIMENTO.....")
        print("==============================")
        resultado = int(input("Digite o resultado do jogo (1 para Jogador 1, 2 para Jogador 2, 3 para empate): "))
        if resultado == 1:
            vitoria_1 += 1
            print(f"Jogador {jogador_1} venceu!")
        elif resultado == 2:
            vitoria_2 += 1
            print(f"Jogador {jogador_2} venceu!")
        elif resultado == 3:
            empates += 1
            print("Empate!")
        else:
            print("Resultado inválido.")
    elif opcao == "2":
        print("==============================")
        print("REGRAS EM DESENVOLVIMENTO.....")
        print("==============================")

    elif opcao == "3":
        print("==============================")
        print("Placar:")
        if jogador_1 == "":
            print(f"Jogador 1: {vitoria_1} vitórias")
        else:
            if vitoria_1 == 1:
                print(f"{jogador_1}: {vitoria_1} vitória")
            else:
                print(f"{jogador_1}: {vitoria_1} vitórias")
        if jogador_2 == "":
            print(f"Jogador 2: {vitoria_2} vitórias")
        else:
            if vitoria_2 == 1:
                print(f"{jogador_2}: {vitoria_2} vitória")
            else:
                print(f"{jogador_2}: {vitoria_2} vitórias")
        print(f"Empates: {empates}")
        print("==============================")
    
    elif opcao != "4":
        print("Opção inválida. Selecione uma opção novamente.")

print("Saindo do jogo. Até a próxima!")
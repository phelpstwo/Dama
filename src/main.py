#MENU JOGO DE DAMA
opcao_menu = None
opcao_aux = None
nome_jogador1 = ""
nome_jogador2 = ""
qtd_vitorias1 = 0
qtd_vitorias2 = 0
empates = 0

while opcao_menu != "4":
    
    print("\n" * 50)
    print("====================================")
    print("Bem-vindo ao Jogo de Dama!")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Placar")
    print("4 - Sair")
    print("====================================")
    opcao_menu = input("Escolha uma opção: ")
    print("\n" * 50)
    
    if opcao_menu == "1":
        opcao_aux = None
        
        while opcao_aux != "4":
            print("\n" * 50)
            print("========[Nome dos Jogadores]========")
            nome_jogador1 = input("Jogador 1: ")
            nome_jogador2 = input("Jogador 2: ")
            print("\n" * 50)
            print(f"\nSeja bem-vindo(a) {nome_jogador1} e {nome_jogador2}!")
            print("Iniciando o jogo de dama...")
            print("==============================")
            print("JOGO EM DESENVOLVIMENTO.....")
            print("==============================")
            opcao_aux = input("Digite o resultado do jogo (1 para Jogador 1, 2 para Jogador 2, 3 para empate ou 4 para sair): ")
            
            if opcao_aux == "1":
                qtd_vitorias1 += 1
                print(f"Jogador {nome_jogador1} venceu!")
            elif opcao_aux == "2":
                qtd_vitorias2 += 1
                print(f"Jogador {nome_jogador2} venceu!")
            elif opcao_aux == "3":
                empates += 1
                print("Empate!")
            elif opcao_aux == "4":
                break
            else:
                print("Resultado inválido.")
                
    elif opcao_menu == "2":
        opcao_aux = None
        
        while opcao_aux != "1":
            print("\n" * 50)
            print("============= [Regras] =============")
            print("REGRAS EM DESENVOLVIMENTO.....\n")
            print("1 - Voltar ao menu inicial")
            print("====================================")
            opcao_aux = input("Escolha uma opção: ")
            
            if opcao_aux == "1":
                break
            else:
                print("\n" * 50)
                print("====================================================")
                print("Opção inválida! Escolha uma opção do menu novamente.")
                print("====================================================")
                input("Pressione Enter para continuar...")

    elif opcao_menu == "3":
        opcao_aux = None
        
        while opcao_aux != "1":
            print("\n" * 50)
            print("============= [Placar] =============")    
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
            print(f"Empates: {empates}\n")
            print("1 - Voltar ao menu inicial")
            print("====================================")
            opcao_aux = input("Escolha uma opção: ")
                
            if opcao_aux == "1":
                break
            else:
                print("\n" * 50)
                print("====================================================")
                print("Opção inválida! Escolha uma opção do menu novamente.")
                print("====================================================")
                input("Pressione Enter para continuar...")
    
    elif opcao_menu != "4":
        print("\n" * 50)
        print("====================================================")
        print("Opção inválida! Escolha uma opção do menu novamente.")
        print("====================================================")
        input("Pressione Enter para continuar...")

print("Saindo do jogo. Até a próxima!")
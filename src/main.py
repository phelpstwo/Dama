opcao_menu = None
opcao_aux = None

nome_jogador1 = ""
nome_jogador2 = ""
qtd_vitorias1 = 0
qtd_vitorias2 = 0
empates = 0
total_partidas = 0
series_ganhas1 = 0
series_ganhas2 = 0

limites_sem_captura = 20

tabuleiro = [
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

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
        voltar_menu = False
        while not voltar_menu:
            while nome_jogador1 == "" or nome_jogador2 == "":
                print("\n" * 50)
                print("========[Nome dos Jogadores]========")
                nome_jogador1 = input("Jogador 1: ")
                nome_jogador2 = input("Jogador 2: ")
                print("\n" * 50)
                
                if nome_jogador1 == "" or nome_jogador2 == "":
                    print("\n" * 50)
                    print("============================================")
                    print("O nome dos jogadores não pode ficar vazio!")
                    print("============================================")
                    input("Pressione Enter para continuar...")
                    
            if nome_jogador1 != "" and nome_jogador2 != "":
                print("\n" * 50)
                print(f"[ 200 OK ] : Sejam bem-vindos(as) {nome_jogador1} e {nome_jogador2}!\n")
                print("======== [Série de partidas] ========\n")
                print("1 - Partida única")
                print("2 - Melhor de 3")
                print("3 - Melhor de 5")
                print("4 - Voltar")
                print("=====================================")
                opcao_aux = input("Escolha uma opção: ")
                print("\n" * 50)
                
                if opcao_aux == "1" or opcao_aux == "2" or opcao_aux == "3":
                    
                    partida_unica = False
                    if opcao_aux == "1":
                        partida_unica = True
                        vit_necessarias = 1
                        nome_serie = "Partida única"
                    elif opcao_aux == "2":
                        vit_necessarias = 2
                        nome_serie = "Melhor de 3"
                    elif opcao_aux == "3":
                        vit_necessarias = 3
                        nome_serie = "Melhor de 5"
                        
                    serie_encerrada = False
                    vit_serie1 = 0
                    vit_serie2 = 0
                    n_partida = 0
                    
                    while vit_serie1 < vit_necessarias and vit_serie2 < vit_necessarias and not serie_encerrada:
                        n_partida += 1
                        
                        for i in range(6):
                            for j in range(6):
                                tabuleiro[i][j] = "."
                                if (i + j) % 2 == 1:
                                    if i < 2:
                                        tabuleiro[i][j] = "o"
                                    elif i > 3:
                                        tabuleiro[i][j] = "x"
                                        
                        terminou = False
                        turno = 1
                        vencedor = 0
                        jogadas = 0
                        em_sequencia = False
                        sem_captura = 0
                        
                        while not terminou:
                            if turno == 1:
                                nome_vez = nome_jogador1
                                peca = "x"
                                dama = "X"
                                peca_adv = "o"
                                dama_adv = "O"
                            else:
                                nome_vez = nome_jogador2
                                peca = "o"
                                dama = "O"
                                peca_adv = "x"
                                dama_adv = "X"
                                
                            existe_captura = False
                            for i in range(6):
                                for j in range(6):
                                    if tabuleiro[i][j] == peca or tabuleiro[i][j] == dama:
                                        for desloc_l in range(-2, 3):
                                            for desloc_c in range(-2, 3):
                                                if (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                                    alvo_l = i + desloc_l
                                                    alvo_c = j + desloc_c
                                                    if alvo_l >= 0 and alvo_l < 6 and alvo_c >= 0 and alvo_c < 6:
                                                        meio = tabuleiro[i + desloc_l // 2][j + desloc_c // 2]
                                                        if tabuleiro[alvo_l][alvo_c] == "." and (meio == peca_adv or meio == dama_adv):
                                                            existe_captura = True
                            
                            print("\n" * 50)
                            print(f"Série: {nome_serie}")
                            print(f"Vez: {nome_vez}")
                            print(f"Peças: {peca}/{dama}\n")
                            
                            cabecalho = "    "
                            for colunas_exibida in range(6):
                                cabecalho += f"  {colunas_exibida + 1}  "
                            print(cabecalho)
                            for linhas_exibidas in range(6):
                                linha_texto = f"{linhas_exibidas + 1} | "
                                for colunas_exibidas in range(6):
                                    if tabuleiro[linhas_exibidas][colunas_exibidas] == ".":
                                        linha_texto += "[   ]"
                                    else:
                                        linha_texto += f"[ {tabuleiro[linhas_exibidas][colunas_exibidas]} ]"
                                print(linha_texto)
                            print()
                            if existe_captura:
                                print("Atenção: você tem uma captura obrigatória, aproveite!")
                                
                            valida_jogada = False
                            while not valida_jogada:
                                if not em_sequencia:
                                    valida_entrada = False
                                    while not valida_entrada:
                                        entrada = input("Linha de origem (1 a 6): ")
                                        for numero in range(1, 7):
                                            if entrada == str(numero):
                                                orig_l = numero - 1
                                                valida_entrada = True
                                        if not valida_entrada:
                                            print("Entrada inválida! Digite um número de 1 a 6.")

                                    valida_entrada = False
                                    while not valida_entrada:
                                        entrada = input("Coluna de origem (1 a 6): ")
                                        for numero in range(1, 7):
                                            if entrada == str(numero):
                                                orig_c = numero - 1
                                                valida_entrada = True
                                        if not valida_entrada:
                                            print("Entrada inválida! Digite um número de 1 a 6.")
                                else:
                                    print(f"Continue capturando com a peça da linha {orig_l + 1} e coluna {orig_c + 1}.")

                                valida_entrada = False
                                while not valida_entrada:
                                    entrada = input("Linha de destino (1 a 6): ")
                                    for numero in range(1, 7):
                                        if entrada == str(numero):
                                            dest_l = numero - 1
                                            valida_entrada = True
                                    if not valida_entrada:
                                        print("Entrada inválida! Digite um número de 1 a 6.")

                                valida_entrada = False
                                while not valida_entrada:
                                    entrada = input("Coluna de destino (1 a 6): ")
                                    for numero in range(1, 7):
                                        if entrada == str(numero):
                                            dest_c = numero - 1
                                            valida_entrada = True
                                    if not valida_entrada:
                                        print("Entrada inválida! Digite um número de 1 a 6.")
                                        
                                peca_jogador = tabuleiro[orig_l][orig_c]
                                valida_peca = peca_jogador == peca or peca_jogador == dama
                                valida_dama = peca_jogador == "X" or peca_jogador == "O"
                                desloc_l = dest_l - orig_l
                                desloc_c = dest_c - orig_c
                                
                                direcao_correta = False
                                if valida_dama:
                                    direcao_correta = True
                                elif turno == 1 and desloc_l < 0:
                                    direcao_correta = True
                                elif turno == 2 and desloc_l > 0:
                                    direcao_correta = True
                                    
                                captura = False
                                if valida_peca and tabuleiro[dest_l][dest_c] == ".":
                                    if (desloc_l == 1 or desloc_l == -1) and (desloc_c == 1 or desloc_c == -1):
                                        if direcao_correta and not existe_captura:
                                            valida_jogada = True
                                    elif (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                        meio_l = (orig_l + dest_l) // 2
                                        meio_c = (orig_c + dest_c) // 2
                                        if tabuleiro[meio_l][meio_c] == peca_adv or tabuleiro[meio_l][meio_c] == dama_adv:
                                            valida_jogada = True
                                            captura = True
                                            
                                if not valida_jogada:
                                    print("Atenção: movimento inválido! Use uma peça sua e uma casa livre na diagonal")
                                    print("(1 casa) ou salte sobre uma peça adversária.")
                                    if existe_captura:
                                        print("Lembre-se: existe captura disponível e ela é obrigatória.")

                            tabuleiro[orig_l][orig_c] = "."
                            tabuleiro[dest_l][dest_c] = peca_jogador
                            em_sequencia = False

                            if captura:
                                tabuleiro[meio_l][meio_c] = "."
                                sem_captura = 0

                                for desloc_l in range(-2, 3):
                                    for desloc_c in range(-2, 3):
                                        if (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                            alvo_l = dest_l + desloc_l
                                            alvo_c = dest_c + desloc_c
                                            if alvo_l >= 0 and alvo_l < 6 and alvo_c >= 0 and alvo_c < 6:
                                                meio = tabuleiro[dest_l + desloc_l // 2][dest_c + desloc_c // 2]
                                                if tabuleiro[alvo_l][alvo_c] == "." and (meio == peca_adv or meio == dama_adv):
                                                    em_sequencia = True
                            else:
                                sem_captura += 1

                            if em_sequencia:
                                orig_l = dest_l
                                orig_c = dest_c
                            else:
                                if peca_jogador == "x" and dest_l == 0:
                                    tabuleiro[dest_l][dest_c] = "X"
                                elif peca_jogador == "o" and dest_l == 5:
                                    tabuleiro[dest_l][dest_c] = "O"
                                jogadas += 1

                                proximo = 3 - turno
                                if proximo == 1:
                                    prox_peca_jogador = "x"
                                    prox_dama = "X"
                                    prox_adv = "o"
                                    prox_adv_dama = "O"
                                else:
                                    prox_peca_jogador = "o"
                                    prox_dama = "O"
                                    prox_adv = "x"
                                    prox_adv_dama = "X"

                                pecas = 0
                                movimentos = 0
                                for i in range(6):
                                    for j in range(6):
                                        casa = tabuleiro[i][j]
                                        if casa == prox_peca_jogador or casa == prox_dama:
                                            pecas += 1
                                            casa_dama = casa == "X" or casa == "O"
                                            for desloc_l in range(-2, 3):
                                                for desloc_c in range(-2, 3):
                                                    alvo_l = i + desloc_l
                                                    alvo_c = j + desloc_c
                                                    if alvo_l >= 0 and alvo_l < 6 and alvo_c >= 0 and alvo_c < 6:
                                                        if tabuleiro[alvo_l][alvo_c] == ".":
                                                            if (desloc_l == 1 or desloc_l == -1) and (desloc_c == 1 or desloc_c == -1):
                                                                if casa_dama or (proximo == 1 and desloc_l < 0) or (proximo == 2 and desloc_l > 0):
                                                                    movimentos += 1
                                                            elif (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                                                meio = tabuleiro[i + desloc_l // 2][j + desloc_c // 2]
                                                                if meio == prox_adv or meio == prox_adv_dama:
                                                                    movimentos += 1

                                if movimentos == 0:
                                    vencedor = turno
                                    terminou = True
                                    if pecas == 0:
                                        motivo_fim = "O adversário ficou sem peças."
                                    else:
                                        motivo_fim = "O adversário ficou sem movimentos."
                                elif sem_captura >= limites_sem_captura:
                                    vencedor = 0
                                    terminou = True
                                    motivo_fim = f"{limites_sem_captura} jogadas seguidas sem captura."
                                else:
                                    turno = proximo
                                    
                        print("\n" * 50)
                        print(f"========= FIM DA PARTIDA {n_partida} =========\n")
                        cabecalho = "    "
                        for coluna_final in range(6):
                            cabecalho += f"  {coluna_final + 1}  "
                        print(cabecalho)
                        for linha_final in range(6):
                            linha_texto = f"{linha_final + 1} | "
                            for coluna_final in range(6):
                                if tabuleiro[linha_final][coluna_final] == ".":
                                    linha_texto += "[   ]"
                                else:
                                    linha_texto += f"[ {tabuleiro[linha_final][coluna_final]} ]"
                            print(linha_texto)
                        print()

                        total_partidas += 1
                        if vencedor == 1:
                            vit_serie1 += 1
                            qtd_vitorias1 += 1
                            print(f"Vencedor da partida: {nome_jogador1}")
                        elif vencedor == 2:
                            vit_serie2 += 1
                            qtd_vitorias2 += 1
                            print(f"Vencedor da partida: {nome_jogador2}")
                        else:
                            empates += 1
                            print("A partida terminou empatada!")
                        print(motivo_fim)
                        print(f"\nPlacar da série ({nome_serie}): {nome_jogador1} {vit_serie1} x {vit_serie2} {nome_jogador2}")
                        print(f"Placar acumulado: {nome_jogador1} {qtd_vitorias1} x {qtd_vitorias2} {nome_jogador2} | Empates: {empates}")
                        input("\nPressione Enter para continuar...")
                        
                        if partida_unica:
                            serie_encerrada = True
                    if not partida_unica:
                        print("\n" * 50)
                        print("========= FIM DA SÉRIE =========\n")
                        if vit_serie1 == vit_necessarias:
                            series_ganhas1 += 1
                            print(f"Campeão da série {nome_serie}: {nome_jogador1}!")
                        else:
                            series_ganhas2 += 1
                            print(f"Campeão da série {nome_serie}: {nome_jogador2}!")
                        print(f"Resultado: {vit_serie1} x {vit_serie2}")
                        input("\nPressione Enter para voltar ao menu de séries...")
                 
                elif opcao_aux == "4":
                    voltar_menu = True
                else:
                    print("\n" * 50)
                    print("====================================================")
                    print("Opção inválida! Escolha uma opção do menu novamente.")
                    print("====================================================")
                    input("Pressione Enter para continuar...")
                
    elif opcao_menu == "2":
        opcao_aux = None
        
        while opcao_aux != "1":
            print("\n" * 50)
            print("====================== [Regras] ======================")
            print("1 ~ Peça comum anda uma casa na diagonal, para frente.")
            print("2 ~ A captura é obrigatória.")
            print("3 ~ A captura é feita com um salto de duas casas sobre")
            print("a peça adversária, para frente ou para trás.")
            print("4 ~ Se a mesma peça puder capturar novamente, ela deve")
            print("continuar a jogada.")
            print("5 ~ Ao chegar na última linha do adversário, a peça   ")
            print("comum vira dama (X ou O).")
            print("6 ~ A dama anda e captura nas 4 diagonais.")
            print("7 ~ Vence quem eliminar ou bloquear o adversário.")
            print("8 ~ Vence séries de partida única, melhor de 3 e melhor")
            print("de 5, quem garantir a maioria das vitórias.")
            print("9 ~ Empate é dado após 20 jogadas seguidas sem cap-")
            print("tura.")
            print("10 ~ Empate não é contabilizado para na série.\n")
            print("1 - Voltar ao menu inicial")
            print("======================================================")
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

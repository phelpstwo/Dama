# =====================================================================
#                    JOGO DE DAMAS 6x6 NO TERMINAL
# =====================================================================
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
    # =====================================================================
    #                             MENU DO JOGO
    # =====================================================================
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
        # =====================================================================
        #                              1 - JOGAR
        # =====================================================================
        opcao_aux = None
        voltar_menu = False
        while not voltar_menu:
            # > Pede aos jogadores inserirem seu nome apenas uma vez.
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
                    
            # =====================================================================
            #                            MENU DE SÉRIES
            # =====================================================================
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
                    
                    # > Extrai dados de cada tipo de série e os utiliza tanto durante quanto após o fim da mesma.
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
                    
                    # =====================================================================
                    #                          INÍCIO DAS SÉRIES
                    # =====================================================================
                    # > Continua a série até alguém garantir a maioria das vitórias.
                    # > Encerra o laço em caso de empate em partida única.
                    while vit_serie1 < vit_necessarias and vit_serie2 < vit_necessarias and not serie_encerrada:
                        n_partida += 1
                        # > Insere peças no tabuleiro, seguindo a lógica de que todas as peças ficam na
                        #   posição em que a soma da linha com a coluna é sempre ímpar.
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
                        
                        # =====================================================================
                        #                        ALTERNAÇÃO ENTRE TURNOS
                        # =====================================================================
                        # > Continua na série até alguém vencer ou houver empate, caso contrário pula
                        #   para o próximo turno.
                        while not terminou:
                            # > Extrai dados dos jogadores e os utiliza na execução de cada jodada.
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
                                
                            # =====================================================================
                            #                     EXISTE CAPTURA PARA O JOGADOR?
                            # =====================================================================
                            # > Verifica se existe alguma captura disponível para o jogador do turno.
                            existe_captura = False
                            # > Percorre as linha e colunas do tabuleiro.
                            for i in range(6):
                                for j in range(6):
                                    # > Verifica se na casa existe alguma peça.
                                    if tabuleiro[i][j] == peca or tabuleiro[i][j] == dama:
                                        # > Faz todos os deslocamentos possíveis de 2 casas.
                                        for desloc_l in range(-2, 3):
                                            for desloc_c in range(-2, 3):
                                                # > Filtra apenas os deslocamentos nas 4 diagonais.
                                                if (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                                    alvo_l = i + desloc_l
                                                    alvo_c = j + desloc_c
                                                    # > Filtra apenas os deslocamentos dentro do tabueliro.
                                                    if alvo_l >= 0 and alvo_l < 6 and alvo_c >= 0 and alvo_c < 6:
                                                        meio = tabuleiro[i + desloc_l // 2][j + desloc_c // 2]
                                                        # > Verifica se ao fazer o deslocamento de 2 casas, a casa de destino está vaga
                                                        #   e se existe alguma peça adversária na casa do meio.
                                                        if tabuleiro[alvo_l][alvo_c] == "." and (meio == peca_adv or meio == dama_adv):
                                                            existe_captura = True
                            
                            # =====================================================================
                            #                          EXIBIÇÃO DO TABULEIRO
                            # =====================================================================
                            print("\n" * 50)
                            print(f"Série: {nome_serie}")
                            print(f"Vez: {nome_vez}")
                            print(f"Peças: {peca}/{dama}\n")
                            
                            # > Exibe as colunas.
                            cabecalho = "    "
                            for colunas_exibida in range(6):
                                cabecalho += f"  {colunas_exibida + 1}  "
                            print(cabecalho)
                            # > Exibe as linhas juntamente com o tabuleiro.
                            for linhas_exibidas in range(6):
                                linha_texto = f"{linhas_exibidas + 1} | "
                                for colunas_exibidas in range(6):
                                    if tabuleiro[linhas_exibidas][colunas_exibidas] == ".":
                                        linha_texto += "[   ]"
                                    else:
                                        linha_texto += f"[ {tabuleiro[linhas_exibidas][colunas_exibidas]} ]"
                                print(linha_texto)
                            print()
                            
                            # > Após a exibição ou reexibição do tabuleiro, avisa sobre a existência de uma captura, se verdadeiro.
                            if existe_captura:
                                print("Atenção: você tem uma captura obrigatória, aproveite!")
                                
                            # =====================================================================
                            #           LEITURA E VALIDAÇÃO DAS ENTRADAS DAS POSIÇÕES
                            # =====================================================================
                            # > Compara o texto digitado com números convertidos em letras e
                            #   converte para o índice da matriz (0 a 5) com [numero - 1].
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
                                            
                                # > Após uma jogada com a mesma peça, pede apenas a posição de destino da peça para
                                #   a captura e ignora a leitura da sua posição de origem.
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
                                        
                                # =====================================================================
                                #              A PEÇA USADA E O DESLOCAMENTO ESTÃO CORRETOS?
                                # =====================================================================
                                # > Guarda a peça da posição de origem.
                                # > Valida o tipo de peça.
                                # > Armazena o deslocamento da peça.
                                peca_jogador = tabuleiro[orig_l][orig_c]
                                valida_peca = peca_jogador == peca or peca_jogador == dama
                                valida_dama = peca_jogador == "X" or peca_jogador == "O"
                                desloc_l = dest_l - orig_l
                                desloc_c = dest_c - orig_c
                                
                                # =====================================================================
                                #                          VALIDAÇÃO DA DIREÇÃO
                                # =====================================================================
                                # > Permite que peça comum só ande para frente e dama para os dois sentidos.
                                direcao_correta = False
                                if valida_dama:
                                    direcao_correta = True
                                elif turno == 1 and desloc_l < 0:
                                    direcao_correta = True
                                elif turno == 2 and desloc_l > 0:
                                    direcao_correta = True
                                
                                # =====================================================================
                                #                    MOVIMENTO SIMPLES OU DE CAPTURA?
                                # =====================================================================
                                # > Valida movimento comum e de captura.
                                captura = False
                                # > Verifica se a casa de destino está vazia.
                                if valida_peca and tabuleiro[dest_l][dest_c] == ".":
                                    # > Verifica se o deslocamento é de 1 casa.
                                    if (desloc_l == 1 or desloc_l == -1) and (desloc_c == 1 or desloc_c == -1):
                                        # > Verifica se a direção está correta e se não existe
                                        #   captura obrigatória para ser feita.
                                        if direcao_correta and not existe_captura:
                                            valida_jogada = True
                                    # > Verifica se o deslocamento é de 2 casas.
                                    elif (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                        meio_l = (orig_l + dest_l) // 2
                                        meio_c = (orig_c + dest_c) // 2
                                        # > Verifica se na casa do meio existe alguma peça adversária.
                                        if tabuleiro[meio_l][meio_c] == peca_adv or tabuleiro[meio_l][meio_c] == dama_adv:
                                            valida_jogada = True
                                            captura = True
                                            
                                # > Exibe mensagem de movimento inválido após falha na validação da jogada.
                                if not valida_jogada:
                                    print("Atenção: movimento inválido! Use uma peça sua e uma casa livre na diagonal")
                                    print("(1 casa) ou salte sobre uma peça adversária.")
                                    if existe_captura:
                                        print("Lembre-se: existe captura disponível e ela é obrigatória.")

                            # > Armazena a jogada executada para ser exibida posteriormente no tabueleiro.
                            tabuleiro[orig_l][orig_c] = "."
                            tabuleiro[dest_l][dest_c] = peca_jogador
                            em_sequencia = False

                            # =====================================================================
                            #                     EXISTEM MAIS CAPTURAS A FAZER?
                            # =====================================================================
                            # > Verifica se existe mais alguma captura em sequência.
                            if captura:
                                # > Remove peça capturada.
                                tabuleiro[meio_l][meio_c] = "."
                                sem_captura = 0
                                
                                # > Percorre linhas e colunas do tabueliro.
                                for desloc_l in range(-2, 3):
                                    for desloc_c in range(-2, 3):
                                        # > Filtra apenas os deslocamentos nas 4 diagonais.
                                        if (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                            alvo_l = dest_l + desloc_l
                                            alvo_c = dest_c + desloc_c
                                            # > Filtra apenas os deslocamento dentro do tabuleiro.
                                            if alvo_l >= 0 and alvo_l < 6 and alvo_c >= 0 and alvo_c < 6:
                                                meio = tabuleiro[dest_l + desloc_l // 2][dest_c + desloc_c // 2]
                                                # > Verifica se ao fazer o deslocamento de 2 casas, a casa de destino está vaga
                                                #   e se existe alguma peça adversária na casa do meio.
                                                if tabuleiro[alvo_l][alvo_c] == "." and (meio == peca_adv or meio == dama_adv):
                                                    em_sequencia = True
                            else:
                                # > Contabiliza movimentos sem captura para definir o empate.
                                sem_captura += 1

                            # =====================================================================
                            #                      MANTÉM OU FINALIZA O TURNO?
                            # =====================================================================
                            # > Mantém a mesma peça se existir captura obrigatória.
                            if em_sequencia:
                                # > Não finaliza o turno ainda aqui.
                                # > Volta ao início para informar as posições e capturar mais uma peça.
                                orig_l = dest_l
                                orig_c = dest_c
                            else:
                                # > Finaliza o turno aqui.
                                # > Promoção a dama ao chegar aos extremos do tabuleiro.
                                if peca_jogador == "x" and dest_l == 0:
                                    tabuleiro[dest_l][dest_c] = "X"
                                elif peca_jogador == "o" and dest_l == 5:
                                    tabuleiro[dest_l][dest_c] = "O"
                                # > Soma uma jogada às estatísticas.
                                jogadas += 1

                                # > Continua na série se ainda existirem jogadas possíveis, 
                                #   caso contrário pula para o próximo turno.
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

                                # =====================================================================
                                #                       EXISTEM PEÇAS E MOVIMENTOS?
                                # =====================================================================
                                pecas = 0
                                movimentos = 0
                                # > Conta as peças e os movimentos possíveis (passos e capturas) do próximo jogador.
                                #   Se ele não puder jogar, perde.
                                for i in range(6):
                                    for j in range(6):
                                        casa = tabuleiro[i][j]
                                        # > Verifica se existem peças adversárias no tabuleiro.
                                        if casa == prox_peca_jogador or casa == prox_dama:
                                            pecas += 1
                                            casa_dama = casa == "X" or casa == "O"
                                            for desloc_l in range(-2, 3):
                                                for desloc_c in range(-2, 3):
                                                    alvo_l = i + desloc_l
                                                    alvo_c = j + desloc_c
                                                    # > Filtra apenas os deslocamentos dentro do tabuleiro.
                                                    if alvo_l >= 0 and alvo_l < 6 and alvo_c >= 0 and alvo_c < 6:
                                                        # > Verifica se a casa de destino está vazia.
                                                        if tabuleiro[alvo_l][alvo_c] == ".":
                                                            # > Verifica se o deslocamento é de 1 casa. 
                                                            if (desloc_l == 1 or desloc_l == -1) and (desloc_c == 1 or desloc_c == -1):
                                                                # > Peça comum só anda para frente e dama para os sentidos.
                                                                if casa_dama or (proximo == 1 and desloc_l < 0) or (proximo == 2 and desloc_l > 0):
                                                                    movimentos += 1
                                                            # > Verifica se o deslocamento é de 2 casas.
                                                            elif (desloc_l == 2 or desloc_l == -2) and (desloc_c == 2 or desloc_c == -2):
                                                                meio = tabuleiro[i + desloc_l // 2][j + desloc_c // 2]
                                                                # > Verifica se na casa do meio existe alguma peça adversária.
                                                                if meio == prox_adv or meio == prox_adv_dama:
                                                                    movimentos += 1
                                # > Declara vencedor aquele que acabou de jogar se não existirem
                                #   mais movimentos possíveis.
                                if movimentos == 0:
                                    vencedor = turno
                                    terminou = True
                                    if pecas == 0:
                                        motivo_fim = "O adversário ficou sem peças."
                                    else:
                                        motivo_fim = "O adversário ficou sem movimentos."
                                # > Declara empate se o limite de jogadas consecutivas sem captura for atingido.
                                elif sem_captura >= limites_sem_captura:
                                    vencedor = 0
                                    terminou = True
                                    motivo_fim = f"{limites_sem_captura} jogadas seguidas sem captura."
                                # > Caso contrário, apenas pula para o próximo turno.
                                else:
                                    turno = proximo
                                    
                        # =====================================================================
                        #                   FIM DA PARTIDA E SUAS ESTATÍSTICAS
                        # =====================================================================
                        print("\n" * 50)
                        print(f"========= FIM DA PARTIDA {n_partida} =========\n")
                        # > Reexibição do tabuleiro com a(s) peça(s) final(is).
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
                        # =====================================================================
                        #                     FIM DA SÉRIE E SUAS ESTATÍSTICAS
                        # =====================================================================
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
                 
                # > Exibe aviso de entrada inválida no menu de escolhas das séries.
                elif opcao_aux == "4":
                    voltar_menu = True
                else:
                    print("\n" * 50)
                    print("====================================================")
                    print("Opção inválida! Escolha uma opção do menu novamente.")
                    print("====================================================")
                    input("Pressione Enter para continuar...")
                
    elif opcao_menu == "2":
        # =====================================================================
        #                             2 - REGRAS
        # =====================================================================
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
            print("5 ~ Ao chegar na última linha do adversário, a peça")
            print("comum vira dama (X ou O).")
            print("6 ~ A dama anda e captura nas 4 diagonais.")
            print("7 ~ Vence quem eliminar ou bloquear o adversário.")
            print("8 ~ Na série (partida única, melhor de 3 ou de 5),")
            print("vence quem garantir a maioria das vitórias.")
            print(f"9 ~ Empate após {limites_sem_captura} jogadas seguidas sem")
            print("captura.")
            print("10 ~ Empate não é contabilizado para a série.\n")
            print("1 - Voltar ao menu inicial")
            print("======================================================")
            opcao_aux = input("Escolha uma opção: ")

            if opcao_aux != "1":
                print("\n" * 50)
                print("====================================================")
                print("Opção inválida! Escolha uma opção do menu novamente.")
                print("====================================================")
                input("Pressione Enter para continuar...")

    elif opcao_menu == "3":
        # =====================================================================
        #                            3 - PLACAR
        # =====================================================================
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
                    
            print(f"Empates: {empates}")
            print(f"Partidas jogadas: {total_partidas}\n")

            if total_partidas > 0:
                pct_vitorias1 = qtd_vitorias1 * 100 / total_partidas
                pct_vitorias2 = qtd_vitorias2 * 100 / total_partidas
                pct_empates = empates * 100 / total_partidas
                print(f"Aproveitamento de {nome_jogador1}: {pct_vitorias1:.1f}%")
                print(f"Aproveitamento de {nome_jogador2}: {pct_vitorias2:.1f}%")
                print(f"Empates: {pct_empates:.1f}%\n")
            else:
                print("Nenhuma partida jogada ainda.\n")

            print(f"Séries ganhas: {nome_jogador1} {series_ganhas1} x {series_ganhas2} {nome_jogador2}\n")
            print("1 - Voltar ao menu inicial")
            print("====================================")
            opcao_aux = input("Escolha uma opção: ")
                
            if opcao_aux != "1":
                print("\n" * 50)
                print("====================================================")
                print("Opção inválida! Escolha uma opção do menu novamente.")
                print("====================================================")
                input("Pressione Enter para continuar...")
    
    # > Exibe aviso de entrada inválida no menu inicial. 
    elif opcao_menu != "4":
        print("\n" * 50)
        print("====================================================")
        print("Opção inválida! Escolha uma opção do menu novamente.")
        print("====================================================")
        input("Pressione Enter para continuar...")
        
# > Exibe mensagem de saída do jogo.
print("Saindo do jogo. Até a próxima!")
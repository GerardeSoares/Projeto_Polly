import os
import random

# Variáveis Globais
jogarNovamente = "s"
jogadas = 0
QuemJoga = 0
maxJogadas = 9
vitoria = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    os.system("cls")
    print("   0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(jogadas))

def jogadorJoga():
    global jogadas
    global QuemJoga
    global vitoria
    global maxJogadas

    if QuemJoga == 0 and jogadas < maxJogadas:
        L = int(input("Linha..:  "))
        c = int(input("Coluna..: "))
        try:
            while velha[L][c] != " ":
                L = int(input("Linha..:  "))
                c = int(input("Coluna..: "))
            velha[L][c] = "X"
            QuemJoga = 1
            jogadas += 1
        except (ValueError, IndexError):
            print("Jogada inválida")
            os.system("Pause")

def cpuJoga():
    global jogadas
    global QuemJoga
    global vitoria
    global maxJogadas

    if QuemJoga == 1 and jogadas < maxJogadas:
        if jogadas == 0:
            # Se a CPU for a primeira a jogar, faça uma jogada aleatória.
            L = random.randrange(0, 3)
            c = random.randrange(0, 3)
        else:
            L, c = minimax(velha, "O")  # Apenas passando o tabuleiro e o jogador
        while velha[L][c] != " ":
            L, c = minimax(velha, "O")  # Apenas passando o tabuleiro e o jogador
        velha[L][c] = "O"
        jogadas += 1
        QuemJoga = 0

#Essa nova definição tem como objetivo saber quem iria começar se é o usuário ou CPU
def escolherQuemComeca():
    global QuemJoga
    escolha = input("Deseja começar o jogo? (S para sim, outra tecla para não): ").strip().lower()
    if escolha == "s":
        QuemJoga = 0  # O jogador começa
    else:
        QuemJoga = 1  # A CPU começa

        
def minimax(tabuleiro, jogador):
    resultado = verificarVitoria()

    if resultado == "O":
        return None, None
    elif resultado == "X":
        return None, None
    elif resultado == "empate":
        return None, None

    if jogador == "O":
        melhor_valor = -float("inf")
        melhorL = None
        melhorC = None
        for L in range(3):
            for C in range(3):
                if tabuleiro[L][C] == " ":
                    tabuleiro[L][C] = "O"
                    valor = minimax_valor(tabuleiro, "X")
                    tabuleiro[L][C] = " "
                    if valor > melhor_valor:
                        melhor_valor = valor
                        melhorL = L
                        melhorC = C
        return melhorL, melhorC
    else:
        melhor_valor = float("inf")
        melhorL = None
        melhorC = None
        for L in range(3):
            for C in range(3):
                if tabuleiro[L][C] == " ":
                    tabuleiro[L][C] = "X"
                    valor = minimax_valor(tabuleiro, "O")
                    tabuleiro[L][C] = " "
                    if valor < melhor_valor:
                        melhor_valor = valor
                        melhorL = L
                        melhorC = C
        return melhorL, melhorC

def minimax_valor(tabuleiro, jogador):
    resultado = verificarVitoria()

    if resultado == "O":
        return 1
    elif resultado == "X":
        return -1
    elif resultado == "empate":
        return 0

    if jogador == "O":
        melhor_valor = -float("inf")
        for L in range(3):
            for C in range(3):
                if tabuleiro[L][C] == " ":
                    tabuleiro[L][C] = "O"
                    valor = minimax_valor(tabuleiro, "X")
                    tabuleiro[L][C] = " "
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for L in range(3):
            for C in range(3):
                if tabuleiro[L][C] == " ":
                    tabuleiro[L][C] = "X"
                    valor = minimax_valor(tabuleiro, "O")
                    tabuleiro[L][C] = " "
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor


def verificarVitoria():
    velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        il = 0  # verificar Linhas
        ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1
        if vitoria != "n":
            break
        # Agora verificar colunas
        il = 0
        ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1
        if vitoria != "n":
            break
        # diagonal
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria = s
            break
        # Diagonal
        soma = 0
        idiagl = 0  # indice diagonal L/C
        idiagc = 2
        while idiagc >= 0:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1  # O indice de linha eu somo e o de coluna eu subtraiu
            idiagc -= 1
        if soma == 3:
            vitoria = s
            break
    if vitoria == "n" and jogadas == maxJogadas:
        return "empate"
    return vitoria

def Redefinir():
    global velha
    global jogadas
    global QuemJoga
    global maxJogadas
    global vitoria
    jogadas = 0
    QuemJoga = 0
    maxJogadas = 9
    vitoria = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while jogarNovamente == "s":
    escolherQuemComeca() #Chama a função para permitir que o usuário escolha quem começa
    while True:
        tela()
        jogadorJoga()
        vitoria = verificarVitoria()
        if vitoria != "n" or jogadas >= maxJogadas:
            break
        cpuJoga()
        tela()
        vitoria = verificarVitoria()
        if vitoria != "n" or jogadas >= maxJogadas:
            break

    print("FIM DO JOGO")
    tela()
    if vitoria == "X":
        print("RESULTADO: Você venceu!")
    elif vitoria == "O":
        print("RESULTADO: CPU venceu!")
    else:
        print("RESULTADO: Empate")
    jogarNovamente = input("Jogar Novamente? [s/n]: ").lower()
    Redefinir()

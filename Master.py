import random
from verification import *

letras = ['A', 'B', 'C', 'D']
numeros = [1, 2, 3, 4]

def printMatriz(x):     ##FUNÇÃO PARA PRINTAR A MATRIZ
    print('\n')
    print('   ', end= " ")
    for i in range(4):
        print(numeros[i], end=" ")
    print('')
    print('   ', end = " ")
    print('| '*4)
    for i in range(4):
        print(letras[i],'-', end = " ")
        for j in range(4):
            
            print(x[i][j], end= " ")
        print('')
def printPonto(jogador1, pontos1, jogador2, pontos2):       #FUNÇÃO RESPONSAVEL POR PRINTAR OS PONTOS
    print('')
    print('')
    print("-="*5)
    print("{}, {} pontos".format(jogador1, pontos1))
    print("{}, {} pontos".format(jogador2, pontos2))
    print("-="*5)
    print('')

tabuleiro = [[0 for x in range(4)] for y in range(4)]       ##CRIA A MATRIZ COM ZEROS

tabuleiro_inicial = [['X' for x in range(4)] for y in range(4)]     ##CRIA UMA MATRIZ COM X

posicoes = [['a1', 'a2', 'a3', 'a4'],['b1', 'b2', 'b3', 'b4'],['c1', 'c2', 'c3', 'c4'],['d1', 'd2', 'd3', 'd4']]        ##MATRIZ EQUIVALENTE AS POSICOES DO TABULEIRO
posicoes_V = []  ##MATRIZ QUE IRA SER UTILIZADA FUTURAMENTE PARA VERIFICAR SE A POSICAO QUE FOI DIGITADA JA 'SAIU'



cont = 0
contJ = 0
contP2 = 0
T = 0
B = 0
N = 0
pontos1 = 0
pontos2 = 0

'''
LIMITA A QUANTIDADE DE TESOUROS,
BURACOS E NUMEROS INTEIROS
'''

while T < 6:
    i = random.randint(0,3)
    j = random.randint(0,3)
    if tabuleiro[i][j] == 0:
        tabuleiro[i][j] = 1
        T += 1
while B < 3:
    i = random.randint(0,3)
    j = random.randint(0,3)
    if tabuleiro[i][j] == 0:
        tabuleiro[i][j] = 2
        B += 1

'''TRANSFORMA OS NUMEROS GERADOS ALEATORIAMENTE
PELAS LETRAS 'T' E 'B' QUE CORRESPONDEM A TESOURO E
BURACO RESPECTIVAMENTE
'''
for i in range(4):
    for j in range(4):
        if tabuleiro[i][j] == 1:
            tabuleiro[i][j] = 'T'
        if tabuleiro[i][j] == 2:
            tabuleiro[i][j] = 'B'


Verificar(tabuleiro, cont)      ##CHAMA O ARQUIVO QUE CONTEM A VERIFICAÇÃO

print('-='*9)
print('  CAÇA AO TESOURO')
print('-='*9)
print('\nBy: ROBERTO;\n    VINÍCIUS')
inicio = '1'
sair = 0

while inicio == '1' and sair != 16:     #DEFINE O INICIO DO JOGO
    inicio = input("\n\nDigite:\n<1> Iniciar\n<2> Regras\n<0> Sair\n--> ")


    if inicio == '1':       ##INICIA O JOGO

        print("\nGAME STARTED")
        jogador1 = input("\n\nJogador 1, informe seu nome: ").upper()
        jogador2 = input("Jogador 2, informe seu nome: ").upper()
        print("\nVOCÊ DEVE DIGITAR A POSIÇÃO DA SEGUINTE FORMA: a3 ou C2")
        print('\n')
        printMatriz(tabuleiro_inicial)
        printPonto(jogador1, pontos1, jogador2, pontos2)

        contP = 0
        sair = 0
        J2 = 0
        while sair < 16:
            J1 = 0
            contC = 0
            ## JOGADOR 1 ##
            while J1 == 0:

                print('')
                posicao1 = input("{}, Digite uma posição: ".format(jogador1)).lower()
                for i in range(0, len(posicoes_V)):
                    if posicao1 == posicoes_V[i]:
                        contP += 1

                if contP == 0:

                    for i in range(4):
                        for j in range(4):
                            if posicao1 == posicoes[i][j]:
                                posicoes_V.append(posicao1)
                                tabuleiro_inicial[i][j] = tabuleiro[i][j]
                                printMatriz(tabuleiro_inicial)
                                if tabuleiro_inicial[i][j] == 'T':      ##PONTUAÇÃO JOGADOR 1
                                    pontos1 += 100
                                elif tabuleiro_inicial[i][j] == 'B':
                                    if pontos1 != 0:
                                        pontos1 -= 50
                                    else:
                                        pontos1 = 0
                                else:
                                    pontos1 = pontos1
                                contP = 0
                                J1 += 1
                                sair += 1

                            else:
                                contC += 1
                    if contC == 16:
                        print("POSIÇÃO INVÁLIDA")
                        printMatriz(tabuleiro_inicial)
                        contC = 0


                else:
                    print("POSIÇÃO JÁ ESCOLHIDA")
                    printMatriz(tabuleiro_inicial)

                printPonto(jogador1, pontos1, jogador2, pontos2)
                contP = 0
            ## JOGADOR 2 ##
            J2 = 0
            J1 = 0
            contC = 0
            while J2 == 0:
                J2 = 0
                posicao2 = input("\n\n{}, Digite uma posição: ".format(jogador2))
                for i in range(0, len(posicoes_V)):
                    if posicao2 == posicoes_V[i]:
                        contP += 1

                if contP == 0:

                    for i in range(4):
                        for j in range(4):
                            if posicao2 == posicoes[i][j]:
                                posicoes_V.append(posicao2)
                                tabuleiro_inicial[i][j] = tabuleiro[i][j]
                                printMatriz(tabuleiro_inicial)
                                if tabuleiro_inicial[i][j] == 'T':      ##PONTUAÇÃO JOGADOR 2
                                    pontos2 += 100
                                elif tabuleiro_inicial[i][j] == 'B':
                                    if pontos2 != 0:
                                        pontos2 -= 50
                                    else:
                                        pontos2 = 0
                                else:
                                    pontos2 = pontos2
                                J2 += 1
                                sair += 1

                            else:
                                contC += 1
                    if contC == 16:
                        print("POSIÇÃO INVÁLIDA")
                        printMatriz(tabuleiro_inicial)


                else:
                    print("POSIÇÃO JÁ ESCOLHIDA")
                    printMatriz(tabuleiro_inicial)
                printPonto(jogador1, pontos1, jogador2, pontos2)
                contP = 0
        print("-="*4, end = "")
        print("GAME OVER", end = "")        #FIM DO JOGO
        print("=-"*4)
        if pontos1 > pontos2:       #VERIFICA QUEM FOI O GANHADOR
            printPonto(jogador1, pontos1, jogador2, pontos2)
            print("{} foi o vencedor, PARABÉNS {}".format(jogador1, jogador1))
        elif pontos1 < pontos2:
            printPonto(jogador1, pontos1, jogador2, pontos2)
            print("{} foi o vencedor, PARABÉNS {}".format(jogador2, jogador2))
        else:
            printPonto(jogador1, pontos1, jogador2, pontos2)
            print("HOUVE UM EMAPTE")

    elif inicio == '2':     #REGRAS
        print("-="*9)
        print("      REGRAS")
        print("-="*9)
        print('')
        print("O jogo consiste em um tabuleiro 4x4 com 6 Tesouros(T), 3 Buracos(B) \ne numeros que indicam onde existem tesouros que sao gerados aleatoriamente.\n\nCada jogador deve escolher uma posicao válida no tabuleiro.\n\n Se o jogador escolher uma posição INVÁLIDA ou \n uma posição já escolhida ele não perderá a vez.\n\nSobre a pontuação:\n\n Se o jogador encontrar  a Letra 'T'(Tesouro) ele ganhará 100 pontos.\n Se o jogador encontrar a Letra 'B'(Buraco) ele perderá 50.\n Sua pontuação nunca fica negativa.\n Vence o jogador com maior pontuação.")
        inicio = '1'
        continue
    elif inicio == '0':
        sair = 16
    else:       ##SE CASO O USUARIO DIGITAR UMA OPÇÃO QUE NAO ESTEJA NO MENU
        print("Opção inválida")
        inicio = '1'
        continue

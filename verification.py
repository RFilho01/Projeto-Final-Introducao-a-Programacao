def Verificar(tabuleiro, cont):
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i+1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j+1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif i == 0 and j == 3:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i+1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j-1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif i == 3 and j == 0:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i-1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j+1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif i == 3 and j == 3:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i-1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j-1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif i == 0:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i+1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j+1] == 'T':
                        cont += 1
                    if tabuleiro[i][j-1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif i == 3:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i][j+1] == 'T':
                        cont += 1
                    if tabuleiro[i-1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j-1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif j == 0:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i+1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j+1] == 'T':
                        cont += 1
                    if tabuleiro[i-1][j] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            elif j == 3:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i][j-1] == 'T':
                        cont += 1
                    if tabuleiro[i+1][j] == 'T':
                        cont += 1
                    if tabuleiro[i-1][j] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0
            else:
                if tabuleiro[i][j] == 0:
                    if tabuleiro[i+1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j+1] == 'T':
                        cont += 1
                    if tabuleiro[i-1][j] == 'T':
                        cont += 1
                    if tabuleiro[i][j-1] == 'T':
                        cont += 1
                    tabuleiro[i][j] = cont
                    cont = 0

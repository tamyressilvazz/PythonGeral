tabuleiro = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def desenho_tabuleiro(vetor_tabuleiro):
    jogo = ''
    for i in range(len(vetor_tabuleiro)):
        if i == 2 or i == 5 or i == 8:
            jogo += " " + vetor_tabuleiro[i] + " \n"
        else:
            jogo += " " + vetor_tabuleiro[i] + " |"
    return jogo


def check_tabuleiro(vetor_tabuleiro, position):
    resultado = False
    if vetor_tabuleiro[position] == '_':
        resultado = True
    return resultado


def check_victory(vetor_tabuleiro, simbolo):
    resultado = False
    # CHECANDO AS LINHAS
    if vetor_tabuleiro[0] == simbolo and vetor_tabuleiro[1] == simbolo and vetor_tabuleiro[2] == simbolo:
        resultado = True
    elif vetor_tabuleiro[3] == simbolo and vetor_tabuleiro[4] == simbolo and vetor_tabuleiro[5] == simbolo:
        resultado = True
    elif vetor_tabuleiro[6] == simbolo and vetor_tabuleiro[7] == simbolo and vetor_tabuleiro[8] == simbolo:
        resultado = True
    # CHECANDO AS COLUNAS
    elif vetor_tabuleiro[0] == simbolo and vetor_tabuleiro[3] == simbolo and vetor_tabuleiro[6] == simbolo:
        resultado = True
    elif vetor_tabuleiro[1] == simbolo and vetor_tabuleiro[4] == simbolo and vetor_tabuleiro[7] == simbolo:
        resultado = True
    elif vetor_tabuleiro[2] == simbolo and vetor_tabuleiro[5] == simbolo and vetor_tabuleiro[8] == simbolo:
        resultado = True
    # CHECANDO A VERTICAL
    elif vetor_tabuleiro[0] == simbolo and vetor_tabuleiro[4] == simbolo and vetor_tabuleiro[8] == simbolo:
        resultado = True
    elif vetor_tabuleiro[6] == simbolo and vetor_tabuleiro[4] == simbolo and vetor_tabuleiro[2] == simbolo:
        resultado = True
    return resultado


'''EMPATE?'''
def check_empate(vetor_tabuleiro):
    resultado = True
    for i in vetor_tabuleiro:
        if i == '_':
            resultado = False
    return resultado


'''Variáveis do jogo da velha'''

gamer = 1
gamer1 = gamer2 = 0

while True:
    """É a vez do jogador1?"""
    if gamer == 1:
        gamer1 = input('\tJogador 1\n\tDigite uma posição de 1 a 9 : ')
        if check_tabuleiro(tabuleiro, int(gamer1) - 1):
            tabuleiro[int(gamer1) - 1] = 'X'
            gamer = 2
            print(desenho_tabuleiro(tabuleiro))
        else:
            print(desenho_tabuleiro(tabuleiro))
            print('\tPosição está ocupada')
    if check_victory(tabuleiro, 'X'):
        print('\tJogador número 1 ganhou')
        break
    if check_empate(tabuleiro):
        print('\tEMPATOU')
        break
    # É a vez do jogador2?

    if gamer == 2:
        gamer2 = input('\tJogador2\n\tDigite uma posição de 1 a 9 : ')
        if check_tabuleiro(tabuleiro, int(gamer2) - 1):
            tabuleiro[int(gamer2) - 1] = 'O'
            gamer = 1
            print(desenho_tabuleiro(tabuleiro))
        else:
            print(desenho_tabuleiro(tabuleiro))
            print('\tPosição está ocupada')
    if check_victory(tabuleiro, 'O'):
        print('\tJogador2\n\tGANHOU!!!')
        break
    if check_empate(tabuleiro):
        print('EMPATOU!!!')
        break

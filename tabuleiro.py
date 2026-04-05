def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))

tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "] ]


def ValidarVitoria(rodada):
    lista =[
[tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]],
[tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]],
[tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]],
[tabuleiro[0][0], tabuleiro[1][0], tabuleiro[2][0]],
[tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]],
[tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]],
[tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]],
[tabuleiro[2][0], tabuleiro[1][1], tabuleiro[0][2]]
]
    for i in lista:
        if i[0] == rodada and i[1] == rodada and i[2] == rodada:
            interface()
            print("O jogador {} venceu!".format(rodada))
            return True
    return False
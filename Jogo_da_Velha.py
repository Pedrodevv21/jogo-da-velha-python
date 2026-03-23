def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))

tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "] ]

def ValidarVitoria(rodada):
    global parar
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro [0][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro [1][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro [2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro [2][0] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro [2][1] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro [2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro [2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro [0][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

def PegarJogada():
    jogada_valida = False
    while jogada_valida == False:
        try:

            linha = (input("Digite a linha ou S para sair:"))

            if linha.lower() == "s":
                print ("Programa encerrado")
                return None, None
            
            coluna = (input("Digite a coluna ou S para sair: "))

            if coluna.lower() == "s":
                print ("Programa encerrado")
                return None, None
            else:
                linha = int(linha)
                coluna = int (coluna)


            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2 :
                jogada_valida = True

                if tabuleiro[linha][coluna] == " ":
                    jogada_valida = True
                else:
                    jogada_valida = False
                    print("essa posiçao esta ocupada,digite outra linha e coluna vazia")

            else:
             print ("digito errado, digite numeros inteiro de 0 a 2 na linha e na coluna")

        except:
            print("voçe digitou um caractere errado, digite um numero valido")
    return linha, coluna        
    

jogar_novamente = True
qtde_partidas = 0 
while jogar_novamente == True:
    tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "] ]
    jogadas = 0
    rodada = "X"
    parar = False

    qtde_partidas += 1
    print("Partida {}".format(qtde_partidas))

    while parar == False:
    
        if jogadas == 9:
            interface()
            print ("Empate!")
            parar = True
        interface()
        print ("SUA VEZ {}".format(rodada))
        linha, coluna = PegarJogada()

        if linha == None:
             novamente_valido = True
             jogar_novamente = False
             break
        if coluna == None:
             novamente_valido = True
             jogar_novamente = False
             break

        if rodada == "X":
            tabuleiro[linha][coluna] = "X"
            ValidarVitoria(rodada)
            if parar == True:
                break   
            jogadas += 1
            rodada = "O"

        elif rodada == "O":
            tabuleiro[linha][coluna] = "O"
            ValidarVitoria(rodada)
            if parar == True:
                break              
            jogadas += 1
            rodada =  "X"


  
    
    if jogar_novamente == True:
        novamente_valido = False

    while novamente_valido == False:
        try:
            novamente = int (input("Voçe deseja jogar novamente ?  1 pra SIM, 2 pra NÃO: "))
            if novamente == 1:
                jogar_novamente = True
                novamente_valido = True
            elif novamente == 2:
                jogar_novamente = False
                novamente_valido = True
                print ("Programa encerrado")
        except:
            print("voçe digitou um caractere errado, digite um numero valido")
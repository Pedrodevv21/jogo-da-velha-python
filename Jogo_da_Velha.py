import random

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


def VerificarSaida(linha, coluna):
    if linha == None:
        return True
        
    if coluna == None:
        return True
    return False
        
    

def jogada_computador():
    jogada_valida = False
    while jogada_valida == False:
        linha = random.randint(0, 2)
        coluna = random.randint(0,2)
        
        if tabuleiro[linha][coluna] == " ":
            jogada_valida = True

        else:
            jogada_valida = False

    return linha, coluna


jogar_novamente = True
Vitoria_X = 0
Vitoria_O = 0
qtde_partidas = 0 
while jogar_novamente == True:
    tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "] ]
    jogadas = 0
    rodada = "X"
    parar = False

    qtde_partidas += 1
    print("Partida {}".format(qtde_partidas))


    modo_jogo = True 

    while modo_jogo == True:
        try:
            jogar =  int (input ("Voçe deseja jogar com o computador ou com outro jogador ? 1 para jogar com computador, 2 para jogador: "))

            if jogar == 2:
                print ("modo com jogador")
                jogar_novamente = True
                modo_jogo = False
            
            elif jogar == 1:
                print ("Modo computador ")
                jogar_novamente = True
                modo_jogo = False
                
        
 
        except:
            print("voçe digitou um caractere errado, digite um numero valido")


    while parar == False:
    
        if jogadas == 9:
            interface()
            print ("Empate!")
            print ("PLACAR")
            print ("X = {}".format(Vitoria_X))
            print ("O = {}".format(Vitoria_O))
            parar = True
            break
        interface()
        print ("SUA VEZ {}".format(rodada))


        if rodada == "X":
            linha, coluna = PegarJogada()  
            
            Verificar_S = VerificarSaida(linha,coluna)

            if Verificar_S == True:
                novamente_valido = True
                jogar_novamente = False
                break

            tabuleiro[linha][coluna] = "X"
            Validar = ValidarVitoria(rodada)
            if Validar == True:
                Vitoria_X += 1
                print ("PLACAR")
                print ("X = {}".format(Vitoria_X))
                print ("O = {}".format(Vitoria_O))    
                break   
            jogadas += 1
            rodada = "O"

        elif rodada == "O":

            if jogar == 1:
                linha,coluna = jogada_computador()
            elif jogar == 2:
                linha, coluna = PegarJogada()

                Verificar_S = VerificarSaida(linha,coluna)
                if Verificar_S == True:
                    novamente_valido = True
                    jogar_novamente = False
                    break
            
                
            tabuleiro[linha][coluna] = "O"
            Validar = ValidarVitoria(rodada)
            if Validar == True:
                Vitoria_O += 1
                print ("PLACAR")
                print ("X = {}".format(Vitoria_X))
                print ("O = {}".format(Vitoria_O))
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


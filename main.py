from tabuleiro import interface, ValidarVitoria
from jogador import PegarJogada, VerificarSaida, jogada_computador
from jogo import Modos, jogar_de_novo, Exibirplacar
from tabuleiro import tabuleiro

jogar_novamente = True
Vitoria_X = 0
Vitoria_O = 0
qtde_partidas = 0 
while jogar_novamente == True:
    tabuleiro[0] = [" ", " ", " "]
    tabuleiro[1] = [" ", " ", " "]
    tabuleiro[2] = [" ", " ", " "]
    jogadas = 0
    rodada = "X"

    qtde_partidas += 1
    print("Partida {}".format(qtde_partidas))

    jogar = Modos()

    while True:
    
        if jogadas == 9:
            interface()
            print ("DEU VELHA!")
            Exibirplacar(Vitoria_X, Vitoria_O)
            break
        interface()
        print ("SUA VEZ {}".format(rodada))


        if rodada == "X":
            linha, coluna = PegarJogada()  
            
            Verificar_S = VerificarSaida(linha,coluna)

            if Verificar_S == True:
                jogar_novamente = False
                break

            tabuleiro[linha][coluna] = "X"
            Validar = ValidarVitoria(rodada)
            if Validar == True:
                Vitoria_X += 1
                Exibirplacar(Vitoria_X, Vitoria_O)
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
                    jogar_novamente = False
                    break
            
                
            tabuleiro[linha][coluna] = "O"
            Validar = ValidarVitoria(rodada)
            if Validar == True:
                Vitoria_O += 1
                Exibirplacar(Vitoria_X, Vitoria_O)
                break              
            jogadas += 1
            rodada =  "X"

    if jogar_novamente == True:
        jogar_novamente = jogar_de_novo()

  


from Jogo.tabuleiro import interface, ValidarVitoria
from Jogo.jogador import PegarJogada, VerificarSaida, jogada_computador
from Jogo.jogo import Modos, jogar_de_novo, Exibirplacar
from Jogo.tabuleiro import tabuleiro
from Banco_Jogo_velha import salvar_partida, listar_partidas

jogar_novamente = True
Vitoria_X = 0
Vitoria_O = 0
qtde_partidas = 0 

# Inicializa uma nova partida
while jogar_novamente == True:
    tabuleiro[0] = [" ", " ", " "]
    tabuleiro[1] = [" ", " ", " "]
    tabuleiro[2] = [" ", " ", " "]
    jogadas = 0
    rodada = "X"
    resultado = None

    qtde_partidas += 1
    print("Partida {}".format(qtde_partidas))

    jogar = Modos()

    if jogar == 1:
        modo = "CPU"
    else:
        modo = "PVP"

    while True:
    
        if jogadas == 9:
            interface()
            print ("DEU VELHA!")
            Exibirplacar(Vitoria_X, Vitoria_O)
            resultado = "VELHA"
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
                resultado = "X"
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
                resultado = "O"
                break              

            jogadas += 1
            rodada =  "X"

    
    if resultado is not None:
        salvar_partida(resultado, modo, jogadas)

        # Salva resultado da partida no banco e exibe histórico
        listar_partidas()

    if jogar_novamente == True:
        jogar_novamente = jogar_de_novo()





  


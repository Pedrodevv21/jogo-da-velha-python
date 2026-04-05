from tabuleiro import tabuleiro
import random


def PegarJogada():
    while True:
        try:

            linha = (input("Digite a linha ou S para sair:"))

            if linha.lower() == "s":
                print ("Programa encerrado")
                #usuário digitou "S" — retorna None em linha e coluna para sinalizar saída
                return None, None
            
            coluna = (input("Digite a coluna ou S para sair: "))

            if coluna.lower() == "s":
                print ("Programa encerrado")
                return None, None
            else:
                linha = int(linha)
                coluna = int (coluna)


            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2 :

                if tabuleiro[linha][coluna] == " ":
                   return linha,coluna
                else:
                    print("essa posiçao esta ocupada,digite outra linha e coluna vazia")

            else:
             print ("digito errado, digite numeros inteiro de 0 a 2 na linha e na coluna")

        except:
            print("voçe digitou um caractere errado, digite um numero valido")


def VerificarSaida(linha, coluna):
    if linha == None:
        return True
        
    if coluna == None:
        return True
    return False

def jogada_computador():
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0,2)
        
        if tabuleiro[linha][coluna] == " ":
            return linha,coluna

# Define o modo de jogo (CPU ou jogador)
def Modos():
    while True:
        try:
            jogar =  int (input ("Voçe deseja jogar com o computador ou com outro jogador ? 1 para jogar com computador, 2 para jogador: "))
            if jogar == 2:
                print ("modo com jogador")
                break
            
            elif jogar == 1:
                print ("Modo computador ")
                break
   
        except:
            print("voçe digitou um caractere errado, digite um numero valido")
    return jogar

def jogar_de_novo():
    while True:
        try:
            novamente = int (input("Voçe deseja jogar novamente ?  1 pra SIM, 2 pra NÃO: "))
            if novamente == 1:
                return True
            elif novamente == 2:
                print ("Programa encerrado")
                return False
        except:
            print("voçe digitou um caractere errado, digite um numero valido")

def Exibirplacar(Vitoria_X, Vitoria_O):
    print ("PLACAR")
    print ("X = {}".format(Vitoria_X))
    print ("O = {}".format(Vitoria_O))
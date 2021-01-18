#Jogo Do Nim
# Função principal - invoca o menu do jogo
def Nim():
    modo = 0
    while modo > 2 or modo < 1:
        print ("Bem-vindo ao jogo do Nim!")
        print("1 - Partida rápida")
        print("2 - Campeonato")
        modo = int(input("Qual modo você deseja jogar? "))
        
    if modo == 1:
        print("Você escolheu modo partida rápida")
        partida()
    elif modo == 2:
        print("Você escolheu modo Campeonato")
        campeonato()


#-----------------------------------------------------------------------------#
def computador_escolhe_jogada (n, m):
    cont = 0
    n_cont = n
    
    while n_cont % (m + 1) != 0:
        n_cont -= 1
        cont += 1

    
    if cont > m:
        return m
    
    elif cont > 0 and cont < m:
        return cont
    else:
        return m


#______________________________________________________________________________

def usuario_escolhe_jogada (n, m):
    
    n_peças = int(input("Quantas peças eseja retirar? "))
        
    while n_peças <= 0 or n_peças > m or n_peças > n:
        n_peças = int(input("Dica: Você não pode digitar um número maior que \na quantidade de movimentos definidos no inicio do jogo\nou maior que o número de peças restantes. \nDigite uma jogada válida:"))
    
            
    return n_peças


#______________________________________________________________________________

def partida ():
    n = int(input("Quantas peças o tabuleiro terá? ")) #Total de peças no tabuleiro
    m = int(input("Qual o número de peças que podem ser retiradas por jogada? ")) #máximo de peças por jogada
    cont = 0
    vencedor = True
    while n > 0:
        cont += 1
        vez_pc = True #Variável de controle para primeira jogada
        usu = 0
        comp = 0
        while cont < 2:
            if n % (m + 1) == 0:
                print("\nVocê começa!\n")
                usu = usuario_escolhe_jogada (n, m)
                print("Você retirou ",usu)
                n -= usu
                print("Agora resta apenas {} peça(s) no tabuleiro.".format(n))
                
            else:
                print("Computafor começa\n")
                comp = computador_escolhe_jogada (n, m)
                print("O computador retirou ",comp)
                n -= comp
                print("Agora resta apenas {} peça(s) no tabuleiro.".format(n))
                vez_pc = False
                if n == 0:
                        vencedor = False
                        #print("Computador Ganhou")
                
            cont += 1
        
        while cont > 1 and  n > 0:
            if vez_pc == False:
                print("\nSua vez!\n")
                      
                usu = usuario_escolhe_jogada (n, m)
                print("Você retirou ",usu)
                n -= usu
                print("Agora resta apenas {} peça(s) no tabuleiro.".format(n))
                if n == 0:
                    vencedor = True
                    #print("Fim de jogo! Você Ganhou")
                if n > 0:    
                    print("\nVez do computador\n")
                        
                    comp = computador_escolhe_jogada (n, m)
                    print("O computador retirou ",comp)
                    n -= comp
                    print("Agora resta apenas {} peça(s) no tabuleiro.".format(n))
                    if n == 0:
                        vencedor = False
                        #print("Computador Ganhou")
            else:
                print("\nVez do computador\n")
                    
                comp = computador_escolhe_jogada (n, m)
                print("O computador retirou ",comp)
                n -= comp
                print("Agora resta apenas {} peça(s) no tabuleiro.".format(n))
                if n == 0:
                        vencedor = False
                        #print("Computador Ganhou")
                if n > 0:        
                    print("\nSua vez\n")
                          
                    usu = usuario_escolhe_jogada (n, m)
                    print("Você retirou ",usu)
                    n -= usu
                    print("Agora resta apenas {} peça(s) no tabuleiro.".format(n))
                    if n == 0:
                        vencedor = True
                        #print("Você Ganhou")
    if vencedor == True:
        return 1 #Usuário Ganhou
    else:
        return 2#Computador Ganhou
            

#-----------------------------------------------------------------------------#
def campeonato ():
    print("Aquele que obtiver três vitórias primeiro será o noo Rei Nim.")
    rodada = 1
    usuario = 0
    computador = 0
    while rodada <= 3:
        print("\n-------------------{}ª Rodada----------------------------------\n".format(rodada))
        jogo = partida()
        rodada += 1
        if jogo == 1:
            usuario += 1
        else:
            computador += 1
            
    if computador > usuario:
        print("**** Final do campeonato! ****")
        print("Fim de jogo! O computador Ganhou")
        
        print("\nPlacar: Você {} X {} Computador".format(usuario,computador))
    else:
        print("**** Final do campeonato! ****")
        print("Fim de jogo! Você Ganhou")
        
        print("\nPlacar: Você {} X {} Computador".format(usuario,computador))
    
    return 

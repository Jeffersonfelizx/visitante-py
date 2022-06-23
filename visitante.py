# Guess the number (computer)
import random 

def visitante(x): 
    numero_aleatorio = random.randint(1,x)
    visitante = 0
    lista = []


    while(visitante != numero_aleatorio):
        visitante = int(input(f'Visitante escolha o numero entre 1 e {x} :'))
        if visitante < numero_aleatorio: 
            print(f'Desculpe- me o numero atual esta errado, tente novamente um numero mais alto que {visitante} ')
            lista.append(visitante)
        elif visitante > numero_aleatorio: 
            print(f'Desculpe- me o numero atual esta errado, tente novamente um numero mais baixo{visitante} ')
            lista.append(visitante)

    print(f'Parabens voce acertou o numero atual é {numero_aleatorio}')    

visitante(10)

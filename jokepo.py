import random 

def jogar(): 

    G = "Ganhou"
    E = 'Empatou'
    P = 'Perdeu'

    jogar_novamente = 'sim'

    while jogar_novamente == 'sim': 

        usuario = input(f" Digite para jogar :  Pedra, Papel, Tesoura. :").lower()
        Computador = random.choice(['tesoura', 'pedra', 'papel'])

        if usuario == Computador: 
            print(f' {usuario} x {Computador}, Quase, mas desta vez você {E}.')
            jogar_novamente = input('Digite sim, → Para jogar novamente, ou Não → Para sair da aplicação: ').lower()

        elif (usuario == 'papel' and Computador == 'pedra') or (usuario == 'tesoura' and Computador == 'papel') or (usuario == 'pedra' and Computador == 'tesoura'):
            print(f'{usuario} x {Computador}, Parabéns você {G}.')
            jogar_novamente = input('Digite sim, → Para jogar novamente, ou Não → Para sair da aplicação: ').lower()

        elif (usuario == 'pedra' and Computador == 'papel') or (usuario == 'papel' and Computador == 'tesoura') or (usuario == 'tesoura' and Computador == 'pedra'):
            print(f'{usuario} x {Computador}, Oh nao, voce {P}')
            jogar_novamente = input('Digite sim, → Para jogar novamente, ou não → Para sair da aplicação: ').lower()
        else: 
            print(f'Parece que algo não esta correto:  você digitou "{usuario.upper()}"Só e aceito Pedra, Papel, Tesoura. ')
            jogar_novamente = 'sim'
jogar()
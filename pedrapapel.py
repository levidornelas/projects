import random

def pedrapapel():
    print('Bem vindo ao pedra, papel e tesoura!')
    opcoes = ['pedra','papel','tesoura','sair']
    
    
    while True:

        jogadaplayer = input('Escolha pedra, papel, tesoura, ou sair: ')
        
        if jogadaplayer not in opcoes:
            print('Por favor insira uma opção válida. ')
            continue

        if jogadaplayer == 'sair':
            print('Obrigado por jogar!')
            break
        
        #Escolha do computador:
        jogadapc = random.choice(opcoes)

        #Escolhas do jogador:
        if jogadaplayer == jogadapc:
            print('Empate!')

        elif jogadaplayer == 'pedra' and jogadapc == 'tesoura':
            print(f'Você escolheu {jogadaplayer} e o computador escolheu {jogadapc}, parabéns, você ganhou!')
        
        elif jogadaplayer == 'tesoura' and jogadapc == 'papel':
            print(f'Você escolheu {jogadaplayer} e o computador escolheu {jogadapc}, parabéns, você ganhou!')

        elif jogadaplayer == 'papel' and jogadapc == 'pedra':
           print(f'Você escolheu {jogadaplayer} e o computador escolheu {jogadapc}, parabéns, você ganhou!')

        else:
            print(print(f'Você escolheu {jogadaplayer} e o computador escolheu {jogadapc}, você perdeu!'))
        
pedrapapel()

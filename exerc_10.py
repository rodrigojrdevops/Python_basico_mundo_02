from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print('-=' * 20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0: # Computador jogou Pedra
    if jogador == 0: # Jogador jogou Pedra
        print('Empate!')
    elif jogador == 1: # Jogador jogou Papel
        print('Jogador Venceu!')
    elif jogador == 2: # Jogador jogou Tesoura
        print('Computador Venceu!')

elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Venceu!')
 
elif computador == 2: # Computador jogou Tesoura
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empate!')
else:
    print('Jogada inválida! Tente novamente.')
print('-=' * 20)
print('Fim do jogo!')
print('Obrigado por jogar!')
print('-=' * 20)
print('Volte sempre!')
print('-=' * 20)
print('Até a próxima!')
print('-=' * 20)



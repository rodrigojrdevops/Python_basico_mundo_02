#Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)  # Faz o computador "pensar" em um número entre 0 e 10
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi?')
print('-=-' * 20 )
acertou = False
palpites = 0  # Contador de palpites
# Enquanto não acertar, o jogador continuará tentando
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    print('-=-' * 20)
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
            print('-=-' * 20)
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
            print('-=-' * 20)
print('Parabéns! Você acertou com {} tentativas. Eu pensei no número {}.'.format(palpites, computador))

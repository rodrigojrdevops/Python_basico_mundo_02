#Crie um programa que leia dosi valores e mostre um menu na tela: Seu programa deverá realizar a operação solicitada em cada caso. Se a opção for inválida, deverá ser solicitada uma nova opção. O programa só poderá ser encerrado quando a opção 5 for escolhida. No final, mostre o resultado de cada operação.
#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do programa
from time import sleep
print('-=-' * 20)
print('Bem-vindo ao programa de operações matemáticas!')
print('-=-' * 20)
sleep(0.5)
print('Vamos realizar algumas operações com dois números que você escolher.')
print('-=-' * 20)
sleep(0.5)
print('Primeiro, vamos definir os números.')
print('-=-' * 20)
sleep(0.5)
# Solicita os dois números ao usuário
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>>> Qual é a opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é igual a {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('>>>>>> Opção inválida. Tente novamente.')
print('Fim do programa. Volte sempre!')
print('-=-' * 20)
# Crie um programa que leia dois valores e mostre um menu na tela: Seu programa deverá realizar a operação solicitada em cada caso. Se a opção for inválida, deverá ser solicitada uma nova opção. O programa só poderá ser encerrado quando a opção 5 for escolhida.
# No final, mostre o resultado de cada operação.
# [1] Somar     
# Fim do exercício
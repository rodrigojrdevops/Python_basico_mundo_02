#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('--'*30)
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
print('--'*30)
print('Fim do programa!')
print('--'*30)
print('Obrigado por participar!')
print('--'*30)
print('Volte sempre!')
print('--'*30)
print('Até logo!')
print('--'*30)

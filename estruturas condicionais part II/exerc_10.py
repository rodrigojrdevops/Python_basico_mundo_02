#Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. (use while e if)

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
print('--'*30)
print('Fim do programa!')
print('--'*30)
print('Obrigado por participar!')
print('--'*30)
print('Volte sempre!')
print('--'*30)
print('Até logo!')
print('--'*30)
# Fim do programa!

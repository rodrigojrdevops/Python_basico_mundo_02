#Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usúario vai continuar.No final, mostre:
#Qual o total gasto na compra.
#Quantos produtos custam mais de R$1000.
#Qual é o nome do produto mais barato.

total = totmil = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if preço >1000:
        totmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break 
print('{:-^40}'.format('FIM DO PROGRAMA)'))
print(f'O total da COMPRA foi R${total:.2f}')

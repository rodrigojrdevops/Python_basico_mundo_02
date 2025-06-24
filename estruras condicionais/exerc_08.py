#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Digite o ano que a {}ª pessoa nasceu:? '.format(pess)))
    idade = atual - nasc
    print('A pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
        print('A pessoa já atingiu a maioridade')
    else:
        totmenor += 1
        print('A pessoa ainda não atingiu a maioridade')
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))


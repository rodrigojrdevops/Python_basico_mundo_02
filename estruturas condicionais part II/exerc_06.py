#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    cont += 1
print('FIM')
print('-=' * 20)
print('Progressão finalizada com sucesso!')
print(f'Foram mostrados {cont - 1} termos dessa PA.')
print('-=' * 20)
print('Obrigado por usar nosso gerador de PA!')
print('-=' * 20)
print('Volte sempre!')
print('-=' * 20)

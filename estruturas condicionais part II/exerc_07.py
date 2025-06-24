#Melhore o desafio 061 para perguntar se o usuário quer ver mais alguns termos.O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10  # Inicializa com 10 termos
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    print('-=' * 20)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('-=' * 20)
print('Obrigado por usar nosso gerador de PA!')
print('-=' * 20)
print('Volte sempre!')
print('-=' * 20)
print('FIM ')
print('-=' * 20)
print('Progressão finalizada com sucesso!')

#Tabuada v3.0
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. Ao final, mostre a tabuada de todos os números solicitados.

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('=-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')  # Exibe mensagem de encerramento do programa
# O loop continua até que o usuário digite um número negativo
# A tabuada é exibida para cada número digitado pelo usuário
# O uso do f-string permite uma formatação mais clara e legível
# O programa encerra com uma mensagem amigável quando o usuário decide parar
# O loop while é uma estrutura de repetição que continua enquanto a condição for verdadeira
# O uso do break permite interromper o loop de forma controlada quando necessário
# O programa é um exemplo simples de como usar o while e o break juntos
# A tabuada é exibida de forma clara e organizada, facilitando a leitura



#Crie um programa que leia uma frase qualquer e difa se ela é um palindromo, desconsiderando os espaços.#
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))    
if inverso == junto:
    print('A frase {} é um PALÍNDROMO!'.format(frase))
else:
    print('A frase {} NÃO É um PALÍNDROMO!'.format(frase))
# Fim do programa#
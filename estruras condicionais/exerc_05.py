#Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.#

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    # Imprime cada termo da PA
    print('{} ' .format(c), end='->')
print('Fim da PA')    
# Fim do programa#
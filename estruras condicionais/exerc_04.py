#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.#

soma = 0
cont = 0
# Loop para ler 6 números inteiros
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        # Se o número for par, adiciona à soma e incrementa o contador#
       soma += num
       cont += 1
print('Você informou {} números pares e a soma deles é {}'.format(cont, soma))




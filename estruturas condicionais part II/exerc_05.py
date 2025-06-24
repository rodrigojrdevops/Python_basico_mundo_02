#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f = f * c
    c -= 1
print('{}'.format(f))


# Você pode usar a função factorial do módulo math para calcular o fatorial de forma simples.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120 
# Ou, se preferir, pode fazer manualmente:
# f = 1
# for c in range(n, 0, -1):
#     f *= c
# print('O fatorial de {} é {}.'.format(n, f))
# Ou ainda, usando while:
# f = 1
# c = n
# while c > 0:
#     f *= c        
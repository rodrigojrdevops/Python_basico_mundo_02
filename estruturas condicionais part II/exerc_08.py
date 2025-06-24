#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
#Exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...  

print('--'*30)
print('Sequência de Fibonacci')
print('--'*30)
n = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))  
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' ')
cont = 3  # Começa do terceiro termo, pois os dois primeiros já foram impressos
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')
print('--'*30)
print('FIM DO PROGRAMA')
print('--'*30)

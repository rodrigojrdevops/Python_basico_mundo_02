#codigo refatorado#

"""r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')"""

#codigo reaproveitado#
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end = '')
    if r1 == r2 and r2 == r3:
        print('O triangulo é EQUILÁTERO!')
    if r1 != r2 and r2 != r3 and r1 != r3:
        print('O triangulo é ISÓSCELES!')
    else:    
        print('O triangulo é ESCALENO!') 
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')        



  
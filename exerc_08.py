#codigo reaproveitado#

peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual sua altura? (M)'))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc <= imc < 30:
    print('Você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você esta com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA!')
    



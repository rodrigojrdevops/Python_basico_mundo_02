#Cire um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos. 

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo, temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')


# Fim do programa
# O programa lê a idade e o sexo de várias pessoas, contando quantas têm mais de 18 anos, quantos homens foram cadastrados e quantas mulheres têm menos de 20 anos
# O loop continua até que o usuário decida parar, e no final, exibe os totais de cada categoria.
# O uso de condicionais e loops permite que o programa funcione de forma interativa, coletando dados do usuário e respondendo de acordo com as entradas fornecidas
# O programa é encerrado com uma mensagem de conclusão, e os totais são exibidos
# O uso de condicionais e loops permite que o programa funcione de forma interativa,
# coletando dados do usuário e respondendo de acordo com as entradas fornecidas
# O programa é encerrado com uma mensagem de conclusão, e os totais são exibidos



   
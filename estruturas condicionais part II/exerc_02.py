#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.  

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor digite o sexo novamente [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

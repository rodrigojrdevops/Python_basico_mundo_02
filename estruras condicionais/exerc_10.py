#Desenvolva um programa que leia o nome, idade e sexo de 4 pesoas.NO final do programa mostre:
# - A média de idade do grupo #
# - Qual é o nome do homem mais velho #
# - Quantas mulheres têm menos de 20 anos #

somaidade = 0
médiaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(p))).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
# Fim do programa
# Este programa lê os dados de quatro pessoas e calcula a média de idade do grupo, identifica o homem mais velho e conta quantas mulheres têm menos de 20 anos. #
# A lógica é simples: para cada pessoa, lemos o nome, idade e sexo, atualizando as variáveis conforme necessário. #
# A estrutura de repetição 'for' é utilizada para iterar sobre as quatro pessoas,
# e as condições 'if' são usadas para verificar as condições específicas para o homem mais velho
# e as mulheres com menos de 20 anos. #
# No final, exibimos os resultados formatados. #
# O programa é eficiente e fácil de entender, ideal para iniciantes em programação. #
# A formatação da saída é feita com o método 'format', que insere os valores
# A estrutura de repetição 'for' é utilizada para iterar sobre as quatro pessoas
# A condição 'if' é usada para verificar se o sexo é masculino ou feminino e se a idade atende aos critérios estabelecidos
# O uso de variáveis para armazenar os dados permite fácil comparação e atualização
# A formatação da saída é feita com o método 'format', que insere os valores
# O programa é eficiente e fácil de entender, ideal para iniciantes em programação
# A lógica é simples: para cada pessoa, lemos o nome, idade e sexo
# Atualizamos as variáveis conforme necessário
# No final, exibimos os resultados formatados
# O programa é eficiente e fácil de entender, ideal para iniciantes em programação
# A estrutura de repetição 'for' é utilizada para iterar sobre as quatro pessoas
# A condição 'if' é usada para verificar as condições específicas para o homem mais velho
# e as mulheres com menos de 20 anos
# No final, exibimos os resultados formatados
# O programa é eficiente e fácil de entender, ideal para iniciantes em programação
# A formatação da saída é feita com o método 'format', que insere os valores
# A estrutura de repetição 'for' é utilizada para iterar sobre as quatro pessoas
# A condição 'if' é usada para verificar se o sexo é masculino ou feminino e se a idade atende aos critérios estabelecidos
# O uso de variáveis para armazenar os dados permite fácil comparação e atualização
# A formatação da saída é feita com o método 'format', que insere os valores
# O programa é eficiente e fácil de entender, ideal para iniciantes em programação
# A lógica é simples: para cada pessoa, lemos o nome, idade e sexo                          


   

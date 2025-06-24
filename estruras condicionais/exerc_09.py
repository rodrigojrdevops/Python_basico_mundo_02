#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.#

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:  # Se for a primeira pessoa, define maior e menor peso
        maior = peso
        menor = peso
    else:
        if peso > maior:  # Verifica se o peso atual é maior que o maior registrado
            maior = peso
        if peso < menor:  # Verifica se o peso atual é menor que o menor registrado
            menor = peso     
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))
# Fim do programa
# Este programa lê o peso de cinco pessoas e determina o maior e o menor peso entre elas
# A lógica é simples: para cada peso lido, comparamos com os valores já registrados
# Se for o primeiro peso, inicializamos os valores de maior e menor
# Caso contrário, atualizamos os valores conforme necessário
# No final, exibimos os resultados
# O programa é eficiente e fácil de entender, ideal para iniciantes em programação
# A estrutura de repetição 'for' é utilizada para iterar sobre as cinco pessoas
# A condição 'if' é usada para verificar se o peso atual é maior ou menor que os valores registrados
# O uso de variáveis para armazenar os pesos permite fácil comparação e atualização
# A formatação da saída é feita com o método 'format', que insere os valores    
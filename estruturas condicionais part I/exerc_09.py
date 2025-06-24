print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Preço de compras: R$'))    
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))  
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

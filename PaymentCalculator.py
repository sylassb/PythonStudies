# It calculates the price to be paid for a product considering its regular price and payment condition:
# Cash: 10% discount
# Debit Card: 5% discount
# Credit Card 2 installments: regular price
# Credit Card 3 installments: 20% interest


print('{:=^40}'.format(' SYLECA STORE '))
price = float(input('Preço total dos produtos: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))
if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif option == 4:
    total = price + (price * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcela em {totparc}x de R${parcela:.2f} com JUROS')
else:
    total = price
    print('Opção invalida de pagamento,tente novamente')
print(f'Sua compra de R${price:.2f} vai custar R${total:.2f} no final')




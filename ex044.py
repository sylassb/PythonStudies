# Elabore um programa que calcule o valor
# a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS SYLECA '))
price = float(input('Preço das compras: R$ '))
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




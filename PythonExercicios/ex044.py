print('='*5,'GERENCIADOR DE PAGAMENTO','='*5)
val = float(input('Digite o valor do produto [R$]: '))
print('''Informe o metódo de pagamento
[1] Dinheiro / Cheque
[2] À vista no Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão''')
opção = int(input('Qual é a opção?: '))
if opção == 1:
    total = val - val*(10/100)
    print('R$ {}'.format(total))
elif opção == 2:
    total = val - val*(5/100)
    print('R$ {}'.format(total))
elif opção == 3:
    total = val
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = val + val*(20/100)
    totparc = int(input('Quantas parcelas?: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = val
    print('Digite um valor válido!!!')
print('Sua compra de R$ {:.2f} vai custar R$ {} no final'.format(val, total))
print('='*5,'OBRIGADO, VOLTE SEMPRE','='*5)

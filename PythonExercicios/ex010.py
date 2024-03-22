r = float(input('Quantos R$ você quer converter? [R$]: '))
#Valor de dollar a U$ 3.27.
d = (r / 3.27)
print('Você consegue comprar U${:.2f} com R${:.2f}.'.format(d, r))

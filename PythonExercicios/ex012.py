p = float(input('Qual o preço do produto? [R$]: '))
d = p * (5/100)
np = p - d
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p, np))

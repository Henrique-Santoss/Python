d = int(input('Quantos dias alugados?: '))
km = int(input('Quantos Km rodados?: '))
# carro custa R$ 60 por dia e R$ 0.15 por Km rodado.
p = (d*60)+(km*0.15)
print('O total a pagar é de R${:.2f}.'.format(p))

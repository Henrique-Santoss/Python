sal = float(input('Qual é o salário do funcionário R$: '))
# aumento de 15% no salário
aum = sal * (15/100)
nsal = sal + aum
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sal, nsal))

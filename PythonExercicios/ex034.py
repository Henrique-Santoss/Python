sal = float(input('Informe o salário do funcionário [R$]: '))
if sal >= 1250.00:
    nsal = sal + (10/100 * sal)
    print('O novo salário com 10% de aumento foi {}'.format(nsal))
else:
    nsal = sal + (15/100 * sal)
    print('O novo salário com 15% de aumento foi {}'.format(nsal))
print('*'*5, 'FIM', '*'*5)

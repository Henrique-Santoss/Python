print('='*5, 'TABUADA 2.0', '='*5)
print('='*23)
n = int(input('Digite a tabuada que quer ver: '))
for c in range(1, 11, 1):
    #tab = c * n #pode se usar essa formula na formatação
    #print('{} x {:2} = {}'.format(n, c, tab))
    print('{} x {:2} = {}'.format(n, c, n*c))
print('='*23)
print('FIM')

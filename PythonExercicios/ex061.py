print('='*5, 'PROGRESSÃO ARITMÉTICA 2.0', '='*5)
print('='*37)
pt = int(input('Digite o primero termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print('{} → '.format(pt), end='')
    c += 1
    pt += r
print(' Acabou!')
print('='*37)
print('FIM')
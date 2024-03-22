print('='*5, 'PROGRESSÃO ARITMÉTICA 3.0', '='*5)
print('='*37)
pt = int(input('Digite o primero termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print('{} → '.format(pt), end='')
    c += 1
    pt += r
print(' Acabou!')
ut = pt
t = 1
resp = 'S'
while resp != 'N':
    t = int(input('Você quer que aparecam mais quantos termos?: '))
    while t > 0:
        print('{} → '.format(ut), end='')
        t -= 1
        ut += r
        c += 1
    print(' Acabou!')
    ut = ut
    resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()
print('Progressão finalizada com {} termos mostrados.'.format(c - 1))
print('='*37)
print('FIM')
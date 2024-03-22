print('='*5, 'PROGRESSÃO ARITMÉTICA', '='*5)
print('='*33)
pt = int(input('Digite o primero termo: '))
r = int(input('Digite a razão: '))
#f = r * 10 # fazendo com que apareça 10 termos / funcionou mas exite uma formula
f = pt + (10 - 1) * r # usado no video resposta
for pa in range(pt, f + r, r):
    print('{}'.format(pa), end=' → ')
print('Acabou')
print('='*33)
print('FIM')
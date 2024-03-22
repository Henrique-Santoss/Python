'''print('='*5, 'Sequência de Fibonacci', '='*5)
print('='*34)
f = int(input('Digite quantos valores gostaria de ver :'))
n1 = 0
n2 = 1
c = 1
while c <= f:
    print('{} → '.format(n1, n2), end='')
    c += 1
    n1 = n2 + n1
    n2 = n1 + n2
print(' Acabou')
print('='*34)
print('FIM')'''

n = int(input('Quantos termos você quer mostrar? : '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
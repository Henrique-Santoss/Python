from math import factorial
print('='*5, 'FATORIAL', '='*5)
print('='*20)
n = int(input('Digite um número: '))
f = 0
c = n
print('{}! = '.format(n), end='')
while c > 0:
    print('{} X '.format(c), end='')
    c -= 1
f = factorial(n)
print('= {}'.format(f))
print('='*20)
print('FIM')
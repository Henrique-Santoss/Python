'''c = s = maior = menor = 0
resp = 'S'
while resp != 'N':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Você gostaria de continuar? [S/N]: ')).strip().upper()
m = s / c
print('Você digitou {} números e a média foi {:.2f}\nO maior número foi {} e o menor foi {}'.format(c, m, maior, menor))
print('FIM')
'''

c = s = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    c += 1
    s += num
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Você gostaria de continuar? [S/N]: ')).strip().upper()
m = s / c
print('Você digitou {} números e a média foi {:.2f}'.format(c, m))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
print('FIM')

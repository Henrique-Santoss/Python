valores = list()
pares = list()
impares = list()
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}o. valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    pares.sort()
    impares.sort()
valores.append(pares)
valores.append(impares)
print('-='*30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

'''num = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input(f'Digite o {c}o. valor: ')
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
'''

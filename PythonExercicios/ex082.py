valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continaur? [S/N]: ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resp in 'N':
        break

valores.sort()
pares.sort()
impares.sort()
print('-='*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
print('Fim')
'''m = list()
valores = list()
msl = sp = stc = cont = 0

for line in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{line}, {c}]: '))
        valores.append(n)
        if n % 2 == 0:  # caso o n seja par irá para a soma
            sp += n
    if c == 2:  # soma dos valores da 3 coluna
        stc += n
m.append(valores[:])
msl = max(valores[3:6])
print('-='*20)

while True:
    print(f'[ {m[0][cont]:^5} ]', end='')
    cont += 1
    if cont % 3 == 0:
        print()
    if cont == len(m[0]):
        break

print('-='*20)

print(f'A soma dos valores pares é {sp}')
print(f'A soma dos valores da terceira coluna é {stc}')
print(f'o maior valor da segunda linha é {msl}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
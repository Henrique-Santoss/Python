'''m = list()
valores = list()
cont = 0
for line in range(0, 3):
    for c in range(0, 3):
        valores.append(int(input(f'Digite um valor para [{line}, {c}]: ')))
m.append(valores[:])

print('-='*20)

while True:
    print(f'[ {m[0][cont]:<}]', end='')
    cont += 1
    if cont % 3 == 0: #quebra de linha da matriz
        print()
    if cont == len(m[0]): #quando contador == len m[0] fim do programa
        break'''

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='') # usar :^ centraliza o texto
    print()
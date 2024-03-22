lista = list()

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-'*25)

print(f'Você digitou os valores {lista}')
maxvalor = max(lista)
minvalor = min(lista)

print(f'O maior valor digitado foi {maxvalor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maxvalor:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {minvalor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == minvalor:
        print(f'{i}... ', end='')
print()

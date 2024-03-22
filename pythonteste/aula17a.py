a = [2, 3, 4, 7]
#b = a #ligação entre listas
b = a [:] #copia de todos os elemtos
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

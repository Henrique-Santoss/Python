linha = ('-'*30)
print(linha)
texto = 'LISTAGEM DE PREÇO'
print(f'{texto:^30}')
print(linha)
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25.9,
         'transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
'''c = 0
while True:
    print(f'{lista[c]:.<20}',end='')
    c += 1
    print(f'R$ {lista[c]:>6.2f}')
    c += 1
    if c == 18:
        break'''
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}',end='')
    else:
        print(f'R$ {lista[pos]:>6.2f}')
print(linha)

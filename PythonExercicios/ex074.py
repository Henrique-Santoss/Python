from random import randint
'''n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
tupla = (n1, n2, n3, n4, n5)'''
tupla = (randint(0,10), randint(0,10), randint(0,10),
         randint(0,10), randint(0,10),)
maivalor = 0
menvalor = 0
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
'''for c in tupla:
    print(f'{c} ', end='')
    if c == 0:
        maivalor == c
        menvalor == c
    elif c > maivalor:
        maivalor = c
    elif tupla.count(0) <= 0:
        menvalor = sorted(tupla)[0]
print('')
print(f'O maior valor foi {maivalor}')
print(f'O menor valor foi {menvalor}')'''
print('')
print(f'O maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')


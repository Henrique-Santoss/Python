tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: '))) #criação de tupla
print(f'Você digitou os valores {tupla}')
'''if tupla.count(9) <= 0: #verificando se existe valor 9
    v9 = 0 #valor de 9
    print(f'O valor 9 apareceu {v9} vezes')
else:'''
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
'''if tupla.count(3) <= 0: #verificando se existem o valor 3
    v3 = 0 #valor de 3
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu {tupla.index(3) + 1}ª posição')'''
if 3 in tupla:
    print(f'O valor 3 apareceu {tupla.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end='')


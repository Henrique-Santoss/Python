n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# Verificando menor valor
menor = n1
if n2 < n3 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
"""if n1 > n2 and n1 > n3:
    print('O maior valor foi {}'.format(n1))
    if n2 > n3:
        print('O menor valor foi {}'.format(n3))
    else:
        print('O menor valor foi {}'.format(n2))
if n2 > n1 and n2 > n3:
    print('O maior valor foi {}'.format(n2))
    if n1 > n3:
        print('O menor valor foi {}'.format(n3))
    else:
        print('O menor valor foi {}'.format(n1))
if n3 > n1 and n3 > n2:
    print('O maior valor foi {}'.format(n3))
    if n1 > n2:
        print('O menor valor foi {}'.format(n2))
    else:
        print('O menor valor foi {}'.format(n1))"""
print('*'*5, 'FIM', '*'*5)

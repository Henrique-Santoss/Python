tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
         'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR','PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR','FUTURO')
'''c = 0
while True:
    print(f'Na palavra {tupla[c]} temos: ', end='')
    if tupla.count(a) >= 1:
        print('A')
    c += 1
    if c == 12:
        break'''
for p in tupla:
    print(f'Na palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
    print('')
print('FIM')

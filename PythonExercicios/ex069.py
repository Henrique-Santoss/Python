titulo = 'FIM DO PROGRAMA'
print(f'{titulo:=^21}')
tot18 = h = m = 0
while True:
    print('-'*21)
    print(' CADASTRE UMA PESSOA ')
    print('-'*21)
    idade = int(input('Idade: '))
    sexo = ' '
    '''while sexo != 'M' and sexo != 'F':'''
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo in 'M':
        h += 1
    if sexo in 'F' and idade <= 20:
        m += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{titulo}')
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {h} homems cadastrados.')
print(f'E temos {m} mulheres com menos de 20 anos.')
print('Fim')

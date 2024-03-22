mai = 0
min = 0
from datetime import date
atual = date.today().year
print('='*5, 'GRUPO DE MAIORIDADE', '='*5)
print('='*31)
for p in range(0, 7):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(p+1)))
    idade = atual - nasc
    if idade >= 18:
        mai += 1
    else:
        min += 1
print('A quantidade de pessoas com maioridade são {}'.format(mai))
print('A quantidade de pessoas menores de idade são {}'.format(min))
print('='*31)
print('FIM')

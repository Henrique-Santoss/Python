from datetime import date
atual = date.today().year
print('='*5,'CNN - Selecionador de Categoria','='*5)
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade > 0 and idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 26 and idade <= 90:
    print('Classificação: MASTER')
else:
    print('Digite um valor válido!!!')
print('='*5,'FIM','='*5)

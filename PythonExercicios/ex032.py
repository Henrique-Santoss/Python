from datetime import date
ano = int(input('Digite o ano: '))
# Ano Bissexto é a cada 4 anos.
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano Bissexto'.format(ano))
else:
    print('O ano {} não é um ano Bissexto'.format(ano))

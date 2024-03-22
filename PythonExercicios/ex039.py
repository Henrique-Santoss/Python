from datetime import date
print('='*5,'ALISTAMENTO MILITAR','='*5)
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18 and idade > 0:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif idade > 18 and idade < 40:
    saldo = idade - 18
    print('Você já deveria ter se alistado à {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Digite um valor válido')
print('='*5,'FIM','='*5)

print('='*5, 'Empréstimo Bancário', '='*5)
vcasa = int(input('Qual o valor da casa?[R$]: '))
sal = float(input('Qual o valor do salário?[R$]: '))
ano = int(input('Em quantos anos vai querer pagar?: '))
parcela = vcasa / (ano * 12)
min = sal * (30/100)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(vcasa, ano), end='')
print(' a prestação será de R$ {:.2f}'.format(parcela))
if parcela <= min:
    print('Seu empréstimo foi APROVADO!')
else:
    print('Seu empréstimo foi NEGADO!')


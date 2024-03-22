sidade = 0
qmulher = 0
ivelho = 0
print('='*5, 'ANALISADOR COMPLETO', '='*5)
print('='*31)
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if sexo == 'M' and idade > ivelho:
        ivelho = idade
        nvelho = nome
    elif sexo == 'F' and idade <= 20:
        qmulher += 1
m = sidade / 4
print('A média de idade é {:.0f}'.format(m))
print('O nome do homem mais velho é {}'.format(nvelho))
print('A quantidade de mulher abaixo de 21 anos é {}'.format(qmulher))
print('='*31)
print('FIM')

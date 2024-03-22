print('='*5,'RESULTADO FINAL','='*5)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2
if m < 5:
    print('Aluno REPROVADO!')
    print('Média {}'.format(m))
elif m >= 5 and m < 7:
    print('Aluno em RECUPERAÇÃO!')
    print('Média {}'.format(m))
elif m >= 7 and m <= 10:
    print('Aluno APROVADO!')
    print('Média {}'.format(m))
else:
    print('Digite os valores válidos!!!')
print('='*5,'FIM','='*5)

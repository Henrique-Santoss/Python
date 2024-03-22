from random import choice
a1 = str(input('Informe o nome do 1º aluno: '))
a2 = str(input('Informe o nome do 2º aluno: '))
a3 = str(input('Informe o nome do 3º aluno: '))
a4 = str(input('Informe o nome do 4º aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno sorteado foi {}.'.format(escolhido))

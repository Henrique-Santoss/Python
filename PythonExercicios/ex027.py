nome = input('Digite seu nome completo: ').strip().upper()
lista = nome.split()
print('Muito prazer em te conhecer!')
print('Primeiro nome: {}'.format(lista[0]))
print('Último nome: {}'.format(lista[len(lista)-1]))

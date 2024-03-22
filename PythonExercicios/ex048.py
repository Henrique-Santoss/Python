s = 0
cont = 0
print('='*5, 'SOMA IMPARES MULTIPLOS DE TRÊS', '='*5)
for c in range(1, 501, 2): #o n sempre será impar
    #if c % 2 == 1 and c % 3 == 0: #verificando se o n é impar e divisivel por 3
    if c % 3 == 0: # como começou com impar e esta pulando de 2 em 2 não precisa verificar se é impar.
        cont += 1
        s += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
print('FIM')

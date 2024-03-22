s = 0
cont = 0
print('='*5, 'SOMA DOS PARES', '='*5)
print('='*26)
for c in range(0, 6):
    n = int(input('Digite o {}º número: '.format(c+1)))
    # verificando se o número é par.
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, s))
print('='*26)
print('FIM')

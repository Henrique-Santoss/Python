'''n = s = c = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        s += n
        c += 1
    print('='*10)
print('Você digitou {} e a soma entre eles foi {}'.format(c, s))
print('FIM')'''

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} e a soma entre eles foi {}.'.format(cont, soma))

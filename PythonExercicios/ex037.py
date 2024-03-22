n = int(input('Digite um número: '))
print('Qual será a base de conversão?')
conv = int(input('''[1] para Binário
[2] para Octal
[3] para Hexadecimal
Sua opção: '''))
if conv == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif conv == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif conv == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Digite um valor válido!!!')

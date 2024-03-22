print('='*3, 'MENU DE OPÇÕES', '='*3)
print('='*22)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('='*22)
opção = 0
r = 'S'
while opção != '5' and r != 'N':
    print('=' * 8, 'MENU', '=' * 8)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    opção = str(input('Selecione uma opção: '))
    if opção == '1':
        s = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1, n2, s))
    elif opção == '2':
        m = n1 * n2
        print('A multiplicação de {} X {} é igual a {}'.format(n1, n2, m))
    elif opção == '3':
        if n1 > n2:
            print('O PRIMEIRO valor é MAIOR')
        else:
            print('O SEGUNDO valor é MAIOR')
    elif opção == '4':
        print('Os valores anteriores são {} e {}'.format(n1, n2))
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    print('='*22)
    r = str(input('Você quer continuar? [S/N]: ')).strip().upper()
print('='*22)
print('FIM')
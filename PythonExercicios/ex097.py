def escreva(txt):
    l = len(txt) + 4
    '''titulo = txt
    print('~'*l)
    print(f'{titulo:^{l}}')
    print('~'*l)'''
    print('~'*l)
    print(f'  {txt}')
    print(f'~'*l)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
print('-='*10)
while True:
    escreva(str(input('Digite uma mensagem: ')))
    while True:
        resp = str(input('Deseja continuar?: ').strip().upper()[0])
        print('-='*10)
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('<< Volte Sempre >>')

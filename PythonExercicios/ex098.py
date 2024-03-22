from time import sleep


def cont1a10():
    print('-='*15)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(0, 11):
        print(c, end=' ')
        sleep(0)
    print('FIM!')


def cont10a0():
    print('-='*15)
    print('Contagem de 10 até 0 de 2 em 2')
    d = 10
    while d >= 0:
        print(d, end=' ')
        d -= 2
        sleep(0)
    print('FIM!')


def custom():
    print('-='*15)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('-='*15)
    if p < 0:
        p = p * -1
    elif p == 0:
        p = 1
    if i < f:
        c = i
        while c <= f:
            print(c, end=' ')
            sleep(0)
            c += p
        print('FIM!')
    elif i > f or '-' in p:
        d = i
        while d >= f:
            print(d, end=' ')
            sleep(0)
            d -= p
        print('FIM!')
    print('-='*15)


# Programa Principal
cont1a10()
cont10a0()
custom()
print('Volte Sempre')

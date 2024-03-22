from time import sleep
c = ('\033[m',  # 0 sem cor
     '\033[43m',  # 1 amarelo
     '\033[41m',  # 2 vermelho
     '\033[45m',  # 3 azul
     '\033[7m')  # 4 negrito


def title(txt, cor=0):
    l = len(txt) + 4
    print(c[cor], end='')
    print('~'*l)
    print(f'{txt:^{l}}')
    print('~'*l)
    print(c[0], end='')
    sleep(0.5)


def ajuda(com):
    title(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def pyhelp(txt):
    while True:
        title(f'SISTEMA DE AJUDA PyHELP', 1)
        resp = input('Função ou Biblioteca (fim para parar)> ')
        if resp == 'fim':
            title('ATE LOGO!', 2)
            return
        else:
            ajuda(resp)

# Programa Principal
a = pyhelp('Função ou Biblioteca > ')
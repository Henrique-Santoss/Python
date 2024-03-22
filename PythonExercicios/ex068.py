'''from random import randint
c = 0
print('=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*10)
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()
    computador = randint(0, 10)
    s = jogador + computador
    print('-'*20)
    if escolha == 'P' and s % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU PAR')
        print('-'*20)
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
    elif escolha == 'I' and s % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU ÍMPAR')
        print('-' * 20)
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
    else:
        if escolha == 'P' and s % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU ÍMPAR')
            print('-' * 20)
            print('Você PERDEU!')
        elif escolha == 'I' and s % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU PAR')
            print('-' * 20)
            print('Você PERDEU!')
        print('=-' * 10)
        break
    print('=-' * 10)
    c += 1
print(f'GAME OVER! Você venceu {c} vezes.')'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
             print('VOCÊ VENCEU!')
             v += 1
        else:
             print('VOCÊ PERDEU!')
             break
    print('Vamos jogar novamente...')

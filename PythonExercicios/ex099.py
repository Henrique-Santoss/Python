from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    maxv = 0
    for c in range(len(num)):
        print(num[c], end=' ') # em alguns casos pode precisar de flush = True
        sleep(1)
        if c == 0:
            maxv = num[c]
        elif maxv < num[c]:
            maxv = num[c]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maxv}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

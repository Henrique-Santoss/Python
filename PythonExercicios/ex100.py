from random import randint
from time import sleep
numeros = []


# Funções
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar():
    s = 0
    for c in range(len(numeros)):
        if numeros[c] % 2 == 0:
            s += numeros[c]
    print(f'Somando os valores pares de {numeros}, temos {s}.')

# Programa Principal


sorteia()
somapar()

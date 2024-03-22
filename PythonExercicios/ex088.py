from random import randrange
from time import sleep
mega = list()
jogos = list()
titulo = 'JOGA NA MEGA SENA'
print('-'*30)
print(f'{titulo:^30}')
print('-'*30)

palpites = int(input('Quantos jogos você quer que eu sorteie? : '))

for p in range(0, palpites):
    for c in range(0, 6):
        n = randrange(0, 60)
        if n in mega:
            n = randrange(0, 60)
        else:
            mega.append(n)
    jogos.append(mega[:])
    mega.clear()

print(f'-='*3, f' SORTEANDO {palpites} JOGOS', '-='*3)
for p in range(0, palpites):
    print(f'Jogo {p+1}: {jogos[p]}')
    sleep(1)
print(f'-='*5, ' < BOA SORTE! > ', '-='*5)

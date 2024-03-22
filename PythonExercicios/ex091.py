'''from random import randint
from time import sleep
dados = {}
print('Valores sorteados:')
for c in range(1, 5):
    dados['jogador'] = f'Jogador {c}'
    dados['sorteio'] = randint(1, 6)
    print(f'    O {dados["jogador"]} tirou {dados["sorteio"]}.')
    sleep(1)
    dados.copy()
print('Ranking dos jogadores: ')

for k in dados.items():
    print(k)'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

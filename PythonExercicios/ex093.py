tgol = 0
gols = []
part = []
jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c}?: '))
    gols.append(gol)
    tgol += gol
jogador['gols'] = gols.copy()
jogador['total'] = tgol
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {gols[c]}.')
print(f'Foi um total de {tgol}.')

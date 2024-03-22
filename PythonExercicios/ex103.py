def ficha():
    n = str(input('Nome do Jogador: '))
    g = input('Número de Gols: ')
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    return print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Programa Principal
print('-'*30)
ficha()

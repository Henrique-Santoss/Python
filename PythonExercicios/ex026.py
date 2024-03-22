frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra A apareceu {} vezes.'.format(frase.count('A')))
print('A letra A apareceu pela 1ª vez na posição {}.'.format(frase.find('A')+1))
print('A letra A apareceu pela última vez na posição {}.'.format(frase.rfind('A')+1))

print('='*5, 'MAIOR E MENOR DA SEQUÊNCIA', '='*5)
print('='*38)
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa [Kg]: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} Kg'.format(maior))
print('O menor peso foi {} Kg'.format(menor))
print('='*38)
print('FIM')

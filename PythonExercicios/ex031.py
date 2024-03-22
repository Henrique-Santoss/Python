dist = int(input('Digite a a distância em Km: '))
if dist <= 200:
    # Cobrar R$ 0.5 para cada km se for abaixo de 200km
    ate200 = dist * 0.5
    print('O preço da sua passagem é R$ {:.2f}'.format(ate200))
else:
    # Cobrar R$ 0.45 para cada km se for acima de 200km
    mai200 = dist * 0.45
    print('O preço da sua passagem é R$ {:.2f}'.format(mai200))
print('*'*5, 'Fim', '*'*5)
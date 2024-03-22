vel = int(input('Digite a velocidade do veiculo [km/h]: '))
print('O limite de velocidade é 80 km/h')
lvel = (vel - 80)
# O valor da multa é R$ 7,00 por km acima do limite de velocidade.
multa = lvel * 7
if vel > 80:
    print('Você foi MULTADO!')
    print('Você estava a {} km/h em uma via de 80 km/h'.format(vel))
    print('E terá que pagar R$ {:.2f} de multa'.format(multa))
else:
    print('Você estava a {} km/h em uma via de 80 km/h'.format(vel))
    print('Você estava dentro do limite de velocidade')
print('*'*5, 'Fim', '*'*5)

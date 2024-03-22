m = int(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
c = m * 100
mm = m * 1000
print('A medida de {:.1f}m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.'.format(m,km, hm, dam, dm, c, mm))

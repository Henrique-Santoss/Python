l = float(input('Qual é a largura da parede? [m]: '))
alt = float(input('Qual é a altura da parede? [m]: '))
a = l * alt
# cada litro de tinta pinta 2m².
t = a / 2
print('Sua parede tem a dimensão de {:2}x{:2} e sua área é de {:.3f}m².'.format(l, alt, a))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(t))

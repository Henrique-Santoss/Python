from math import radians, sin, cos, tan
ang = int(input('Informe o ângulo [º]: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, tan))

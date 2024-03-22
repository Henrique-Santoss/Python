print('='*5,'IMC','='*5)
peso = float(input('Digite seu peso em [Kg]: '))
altura = float(input('Digite sua altura [m]: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e você está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} e você está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} e você está com OBESIDADE!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e você está com OBESIDADE MÓRBIDA!'.format(imc))
else:
    print('Digite um valor válido')
print('='*5,'FIM','='*5)
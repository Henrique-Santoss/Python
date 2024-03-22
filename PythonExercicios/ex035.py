r1 = int(input('informe o comprimento da primeira reta: '))
r2 = int(input('Informe o comprimento da segunta reta: '))
r3 = int(input('Informe o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Com o valor dessas três retas é possivel formar um triângulo')
else:
    print('Com o valor dessas três retas não é possivel formar um triângulo')
print('*'*5, 'FIM', '*'*5)

print('='*5,'Comparador de Números','='*5)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O PRIMEIRO número é maior.')
elif n2 > n1:
    print('O SEGUNDO número é maior.')
elif n1 == n2:
    print('Os dois valores são IGUAIS.')
else:
    print('Por favor digite um valor válido')
print('='*5,'FIM','='*5)

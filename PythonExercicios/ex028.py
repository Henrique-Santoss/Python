import random
n = random.randint(0, 5)
print('Qual foi o número que o computador pensou?')
nu = int(input('Digite o número entre 0 e 5: '))
print('O número que o computador escolheu foi {}'.format(n))
if nu == n:
    print('Você venceu! PARABÉNS!')
else:
    print('Você perdeu! BOA SORTE NA PRÓXIMA VEZ!')

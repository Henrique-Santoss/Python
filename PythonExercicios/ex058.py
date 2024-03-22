'''from random import randint
c = 0
nu = 11
n = randint(0, 10)
print('Qual foi o número que o computador pensou?')
print('='*42)
while nu != n:
    nu = int(input('Digite o número entre 0 e 10: '))
    if nu == n:
        print('Você venceu! PARABÉNS!')
    else:
        print('Você perdeu! BOA SORTE NA PRÓXIMA VEZ!')
    c += 1
    print('='*42)
print('Foram necessários {} palpites até o jogador ganhar!'.format(c))
'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em  um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

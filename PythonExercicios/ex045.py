import emoji
from random import choice
from time import sleep
print('='*5,'JOKENPÔ','='*5)
print('Escolha seu movimento')
print(emoji.emojize('[1] Pedra :raised_fist:'))
print(emoji.emojize('[2] Papel :hand_with_fingers_splayed:'))
print(emoji.emojize('[3] Tesoura :victory_hand:'))
escolha = int(input('Digite o número escolhido: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!')
print('='*20)
lista = [':raised_fist:', ':hand_with_fingers_splayed:', ':victory_hand:']
comp = choice(lista)
if escolha == 1 and comp == ':raised_fist:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':raised_fist:'), emoji.emojize(':raised_fist:')))
    print('EMPATE')
elif escolha == 1 and comp == ':hand_with_fingers_splayed:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':raised_fist:'), emoji.emojize(':hand_with_fingers_splayed:')))
    print('Você PERDEU')
elif escolha == 1 and comp == ':victory_hand:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':raised_fist:'), emoji.emojize(':victory_hand:')))
    print('Você GANHOU')
elif escolha == 2 and comp == ':raised_fist:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':hand_with_fingers_splayed:'), emoji.emojize(':raised_fist:')))
    print('Você GANHOU')
elif escolha == 2 and comp == ':hand_with_fingers_splayed:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':hand_with_fingers_splayed:'), emoji.emojize(':hand_with_fingers_splayed:')))
    print('EMPATE')
elif escolha == 2 and comp == ':victory_hand:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':hand_with_fingers_splayed:'), emoji.emojize(':victory_hand:')))
    print('Você PERDEU')
elif escolha == 3 and comp == ':raised_fist:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':victory_hand:'), emoji.emojize(':raised_fist:')))
    print('Você PERDEU')
elif escolha == 3 and comp == ':hand_with_fingers_splayed:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':victory_hand:'), emoji.emojize(':hand_with_fingers_splayed:')))
    print('Você GANHOU')
elif escolha == 3 and comp == ':victory_hand:':
    print('Jogador {} X {} Computador'.format(emoji.emojize(':victory_hand:'), emoji.emojize(':victory_hand:')))
    print('EMPATE')
else:
    print('Digite um valor válido!!!!')
print('='*5,'FIM','='*5)
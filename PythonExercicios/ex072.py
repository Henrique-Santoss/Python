ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezeoito', 'Dezenove', 'Vinte')

'''n = int(input('Digite um número entre 0 e 20: '))
while True:
    if n not in range(0, 21):
        n = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {ext[n]}')'''

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {ext[núm]}')

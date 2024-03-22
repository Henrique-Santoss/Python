n = 0
#c = 1
while True:
    n = int(input('Quer ver a tabuaba de qual valor: '))
    print('-'*20)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
        break
    '''while c <= 10:
        print(f'{n} x {c:2} = {n * c:2}')
        c += 1'''
    for c in range (1, 11):
        print(f'{n} x {c:2} = {n*c:2}')
    print('-'*20)
    c = 1
print('FIM')

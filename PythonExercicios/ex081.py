valores = list()
cont = 0
cont5 = 0
num = 0
resp = 'S'
while True:
    num = int(input('Digite um valor: '))
    cont += 1
    valores.append(num)
    if num == 5:
        cont5 += 1
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp in 'N':
        break
valores.sort(reverse=True)
print('-='*30)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {valores}')
if cont5 > 0:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')
print('FIM')

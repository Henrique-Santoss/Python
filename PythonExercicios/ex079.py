valores = list() #lista vazio
while True:
    num = int(input('Digite um valor: '))
    if num in valores: #verificar se o numero ja ta na lista
        print('Valores Duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(num) #irá adicionar na lista
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while resp not in 'SN': #só irá aceitar S ou N
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resp in 'N': #caso a resposta seja Não, sai do laço
        break
print('-='*30)
valores.sort() # arrumando para ordem crescente
print(f'Você digitou os valores {valores}')

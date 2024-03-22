titulo = 'LOJA SUPER BARATÃO'
print('-'*22)
print(f'{titulo:^22}')
print('-'*22)
s = mil = mvalor = c = 0
mbarato = ' '
while True:
    nome = str(input('Nome do Produto: ')).upper().strip()
    valor = float(input('Preço : R$ '))
    c += 1
    s += valor
    if c == 1 or valor < mvalor:
        mbarato = nome
        mvalor = valor
    if valor > 1000:
        mil += 1
    resp = ' '
    resp = str(input('Quer continuar? [S/N]:')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()
    if resp == 'N':
        break
fim = 'FIM DO PROGRAMA'
print(f'{fim:-^22}')
print(f'O total da compra foi R$ {s:.2f}')
print(f'Temos {mil} produtos custando mais R$ 1000.00')
print(f'O produto mais barato foi {mbarato} que custa R$ {mvalor:.2f}')

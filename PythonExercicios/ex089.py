'''alunos = list()
nomes = list()
notas = list()
media = list()
c = 0
while True:
    n = str(input('Nome: ')).strip().upper()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    notas.append(n1)
    notas.append(n2)
    media.append(m)
    nomes.append(n)
    nomes.append(notas[:])
    nomes.append(media[:])
    alunos.append(nomes[:])
    notas.clear()
    media.clear()
    nomes.clear()
    resp = str(input('Quer continuar? : ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? : ')).strip().upper()
    if resp in 'N':
        break
print('-='*30)
print('No. NOME         MÉDIA       ')
print('-'*20)

while c < len(alunos):
    print(f'{c:<3} {alunos[c][0]:<12} {alunos[c][2][0]:3} ')
    c += 1
print('-'*30)

while True:
    nalunos = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-'*30)
    for n, a in enumerate(alunos):
        if n == nalunos:
            print(f'Notas de {alunos[n][0]} são {alunos[n][1]}')
        if n != nalunos:
            print('Tente novamente... ')
    print('-'*30)
    if nalunos == 999:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], [media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME:<10"}{"MÉDIA">8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

'''dados = {} #dicionario dos dados
mulheres = [] #lista com o nome das mulheres
smedia = [] #lista dados pessoas acima media
tidade = cont = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    cont += 1
    tidade += dados["idade"]
    media = tidade / cont
    if "F" in dados["sexo"]:
        mulheres.append(dados["nome"])
    if dados["idade"] > media:
        smedia.append(dados["nome"])
        smedia.append(dados["sexo"])
        smedia.append(dados["idade"])
    while True:
        res = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if res == 'N':
        break
    print('-='*20)
print(f'- O grupo tem {cont} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- Lista de pessoas que estão acima de média:')
print(smedia)
print('-='*20)
print('<< ENCERRADO >>')'''

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).upper()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

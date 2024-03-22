dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situacão'] = 'Aprovado'
'''elif dados["Média"] < 7 and dados["Média"] >= 5:'''
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situacão'] = 'Reprovado'
print('-='*20)
for k, v in dados.items():
    print(f'{k} é igual a {v}')

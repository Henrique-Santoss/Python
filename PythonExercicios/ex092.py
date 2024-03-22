from datetime import date
dados = {}
while True:
    dados['Nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    dados['idade'] = date.today().year - nasc
    dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados["ctps"] == 0:
        break
    else:
        dados['contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: R$ '))
        dados['aposentadoria'] = (dados["contratação"] - nasc) + 35
        break
print('-='*25)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}.')

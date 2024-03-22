'''r = 'S'
s = 'M'
while r == 'S':
    s = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
    if s != 'M' and s != 'F':
        print('Digite um valor válido!!!')
    r = str(input('Você quer continuar [S/N]: ')).upper().strip()
print('FIM')'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))

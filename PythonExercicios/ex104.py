def leiaint(txt):
    while True:
        resp = input(txt)
        if resp.isnumeric():
            return resp
        else:
            print(f'\033[31m ERRO! Digite um númeo inteiro válido. \033[m')


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

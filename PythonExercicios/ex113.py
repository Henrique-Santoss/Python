def leiaint(inteiro):
    while True:
        try:
            resp = int(input(inteiro))
        except ValueError:
            print(f'\033[31m ERRO: por favor, Digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31m Usuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return resp


def leiafloat(real):
    while True:
        try:
            resp = float(input(real))
        except ValueError:
            print(f'\033[31m ERRO: por favor, Digite um númeo real válido. \033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31m Usuário preferiu não digitar esse número. \033[m')
            resp = 0
            return resp
        else:
            return resp


# Programa Principal
i = leiaint('Digite um Inteiro: ')
r = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} é o real foi {r} ')

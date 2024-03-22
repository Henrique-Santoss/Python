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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc

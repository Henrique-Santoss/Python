def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31m ERRO! \'{entrada}\' é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)

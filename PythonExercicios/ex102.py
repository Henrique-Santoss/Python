def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    print('-'*30)
    if show is True:
        for c in range(n, 0, -1):
            f *= c
            if c == 1:
                print(f'{c} ', end='')
                break
            print(f'{c} x ', end='')
        return f'= {f}'
    else:
        for c in range(n, 0, -1):
            f *= c
        return f


# Programa Principal
print(fatorial(5, show=True))

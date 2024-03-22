def nota(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resp = {}
    n = [*n]
    c = s = 0
    resp['total'] = len(n)
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    while c in range(0, len(n)):
        s += n[c]
        c += 1
    m = s / len(n)
    resp['média'] = f'{m:.2f}'
    if sit is False:
        return resp
    else:
        if m > 7:
            resp['situação'] = 'BOA'
            return resp
        if 5 < m < 7:
            resp['situação'] = 'RAZOAVÉL'
            return resp
        if m < 5:
            resp['situação'] = 'RUIM'
            return resp


# Programa Principal
resp = nota(5.5, 5.5, 8, 9.5, 8, 4, 10)
help(nota)

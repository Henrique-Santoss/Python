def metade(preço=0, formato=False):
    """
    -> Função para calcular metade do preço.
    :param preço: Valor informado pelo usuário.
    :param formato: (opcional) Formatação dos valores.
    :return: Resultado da função.
    """
    res = preço / 2
    return res if formato == False else moeda(res)

def dobro(preço=0, formato=False):
    """
    -> Função para calcular o dobro do preço.
    :param preço: Valor informado pelo usuário.
    :param formato: (opcional) Formatação dos valores.
    :return: Resultado da função.
    """
    res = preço * 2
    return res if formato == False else moeda(res)

def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Função para calcular o aumento do preço.
    :param preço: Valor informado pelo usuário.
    :param taxa: Valor da taxa.
    :param formato: (opcional) Formatação dos valores.
    :return: Resultado da função.
    """
    res = preço + (preço * (taxa / 100))
    return res if not formato else moeda(res)

def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Função para calcular a redução do preço.
    :param preço: Valor informado pelo usuário.
    :param taxa: Valor da taxa.
    :param formato: (opcional) Formatação dos valores.
    :return: Resultado da função.
    """
    res = preço - (preço * (taxa / 100))
    return res if not formato else moeda(res)

def moeda(preço=0, moeda='R$'):
    """
    -> Função para formatar o resultado.
    :param preço: Valor informado pelo usuário.
    :param moeda: Texto adicionado antes do preço.
    :return: Resultado da função.
    """
    res = f'{moeda} {preço:.2f}'.replace('.',',')
    return res
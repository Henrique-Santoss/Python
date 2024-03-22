print('='*5, 'DECTOR DE PALÍNDROMO', '='*5)
print('='*32)
frase = str(input('Digite uma frase: ')).strip().upper() #ignorou os espaços antes e depois, e depois tudo em maiusculo
palavras = frase.split() #separou as palavras
junto = ''.join(palavras) #juntou as palavras ignorando os espaçoes no meio
inverso = ''
inverso = junto[::-1] #versão simplificada para inverter as palavras
'''for letra in range(len(junto) - 1, -1, -1): #inverteu as palavras
    inverso += junto[letra]'''
if inverso == junto:
    print('Temos um palímetro!')
else:
    print('A frase digitada não é um palímetro!')
print('='*32)
print('FIM')
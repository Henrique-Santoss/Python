import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print(f'\033[31m Não consegui accessar o site Pudim :(')
else:
    print(f'\033[33m Consegui acessar o site Pudim com sucesso!')

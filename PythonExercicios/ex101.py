def voto():
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


# Programa Principal
print('-'*30)
nasc = int(input('Em que ano você nasceu? : '))
voto()

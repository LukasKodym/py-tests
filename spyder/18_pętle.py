# -*- coding: utf-8 -*-

# %%
##
raw_data = '433!14343463!245465!454546'
result = ''

for char in raw_data:
    if char == '!':
        result += ','
    else:
        result += char
print(result)

# %%
##
suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
##
saldo = 450
print('Saldo początkowe {}'.format(saldo))
for kwota in range(10, 60, 10):
    print('wypłacona kwota {}'.format(kwota))
    saldo -= kwota
    print('saldo {}'.format(saldo))
print('saldo po wypłaceniu {}'.format(saldo))

# %%
##
print('\nWitaj w systemie logowania')
print('*' * 30)
nick = input('podaj swój nick: ')
pin = input('podaj swój pin, {}: '.format(nick))

if len(pin) == 4:
    for num in pin:
        if num not in '0123456789':
            print('podałes nipoprawny kod pin')
            break
    else:
        print('kod ważny')
else:
    print('podałes nieporawny kod pin')

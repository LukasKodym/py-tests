# -*- coding: utf-8 -*-

# %%
##
1 / 0

# %%
##
4 + '4'

# %%
##
int('f')

# %%
##
float('sd')

# %%
##
try:
    1 / 0
except:
    print('nie dzieli się przez zero')

# %%
##
try:
    1 / 0
except ZeroDivisionError:
    print('nie dzieli się przez zero')
except TypeError:
    print('zły typ')

# %%
##
try:
    4 + '4'
except TypeError:
    print('nie można dodawać tekstu do liczby')

# %%
##
try:
    int('sd')
except ValueError:
    print('zły tekst')

# %%
##
while True:
    try:
        x = int(input('Podaj liczbę: '))
        break
    except ValueError:
        print('Nie wprowadziłes poprawnej wartoci.')

# %%
##
with open('text.txt', 'r') as f:
    for line in f:
        print(line)

# %%
##
try:
    with open('text.txt', 'r') as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print('Plik nie istnieje')

# %%
##
raise TypeError('Błąd.')

# %%
##
raise ValueError('Błąd wartoci.')


# %%
##
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Dzielenie przez zero')
    except ValueError:
        print('Musisz wprowadzić liczbę')


# divide(3, 0)
# divide(3, '0')
divide('a', 'gh')

# -*- coding: utf-8 -*-

imie = 'Pawel'
_imie = 'Olek' # peodkrelenie stosuje się do zmiennych systemowych

# 3imie = "Ala" # nie zaczynamy zmiennych od cyfr

imie_3 = 'Ala'

# %%
a = 8
b = 20

c = a * b
print(a * b)

# %% nazwy zmennych opisujące zmienne

przepracowane_godziny = 8
stawka__godzinowa = 20

dzienna_pensja = (przepracowane_godziny * stawka__godzinowa)
print(dzienna_pensja)

# %% typy nazewnictwa

camelCase = 'Python 3.7'
PascalCase = 'Python 3.7'
snake_case = 'Python 3.7' # koncepcja używana w Python
# kebab-case = 'Python 3.7' # nie używane w Python
UPPER = 'Python 3.7' # używane do wartoci stałych

# %% lista unikalnych nazw zmiennych zarezerwowanych przez język Python

import keyword
keyword.kwlist

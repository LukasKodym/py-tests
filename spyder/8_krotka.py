# -*- coding: utf-8 -*-

# elementy typli (krotek) są niemutowalne, nie można ich zmieniać

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Amazon', 'USA', 'Technology', 2)

# %%
name_google = google[0]
google[0] = 'Google Company'

# %%
data = (amazon, google)
print(data)

# %%
a = ('Pawel', 'Krakowiak')
print(a)

# %%
imie = 'Pawel'
nazwisko = 'Krakowiak'

# %%
imie, nazwisko, id_user = ('Pawel', 'Krakowiak', '001')

# %% rozpakowywanie tupli
amazon_name, country, sector, rank = amazon

# %% inny sposob na definiowanie tupli
stocks = 'Amazon', 'Apple', "IBM"
print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Poznan', 'Krakow')
print(nested)

# %%
a = 14
b = 12

c = b
b = a
a = c

print(a, b)

# %%
x, y = 10, 15

x, y = y, x

print(x, y)

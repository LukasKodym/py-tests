# -*- coding: utf-8 -*-

version = 3.7
print(version)

# %%
version > 3
version <= 3

# %%
number = 1200
number > 1000

number == 1200
number == 1000

number != 1200
number != 1000

# %%
if [warunek]:
    [instrukcja]
    
# %%
if 8 > 10:
    print('Tak')
    
# %%
a = 8
if a > 10:
    print('a > 10')
    
# %%
a = 20
if a > 10:
    print('a > 10')
else:
    print('a <= 10')

# %%
age = 27

if age < 18:
    print('Nie masz uprawnień.')
else:
    print('Dostęp przyznany')

# %%
age = 18

if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
else:
    print('Dostęp przyznany')

# %%
age = int(input('Podaj ile masz lat: '))

if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
elif age > 18:
    print('Dostęp przyznany')

# %% częć druga
print('Program uruchomiony...')
print("""Włam się do systemu, zgadując dwucyfrowy kod pin.
Numer pin składa się z cyfr: 0, 1, 2.""")

pin = input('Wprowadź nr pin: ')

if pin == '21':
    print('Brawo, złamałes system.')
elif pin == '20':
    print('Byłes blisko.')
else:
    print('Nie zgadłes!')

# %%
pin = int(input('Wprowadź nr pin: '))

if pin == 21:
    print('Brawo, złamałes system.')
elif pin == 20:
    print('Byłes blisko.')
else:
    print('Nie zgadłes!')
    
# %%
string = ' '

if string:
    print('niepusty ciąg znaków')
else:
    print('pusty ciąg znaków')

# %%
number = 0

if number:
    print('liczba niezerowa')
else:
    print('zero')
    
# %%
default_flag = False

if default_flag:
    print('doszło do defaultu')
else:
    print('nie doszło')

# %%
default_flag = True

if not default_flag:
    print('nie doszło')
else:
    print('doszło do defaultu')
    
# %%
saldo = 10000
klient_zweryfikowany = True

if saldo > 0 and klient_zweryfikowany:
    print('Możesz wyplacic gotówkę')
else:
    print('Nie możesz wypłacić gotówki')

# %%
saldo = 10000
klient_zweryfikowany = True
amount = int(input('Ile chcesz wypłacić gotówki? '))

if saldo > 0 and klient_zweryfikowany and saldo >= amount:
    print('Możesz wyplacic gotówkę')
else:
    print('Nie możesz wypłacić gotówki.\
          Brak wystarczającej kwoty {}'.format(abs(saldo - amount)))

# %%
fakt = 'python jest łatwy i przyjemny'
lenght = len(set(list(fakt)))
if lenght < 20:
    print('Mniej niż 20 unikalnych znaków.')
else:
    print('Liczba unikalnych znaków jest większa lub równa 20.')

# %%
name = 'python'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znaleziono p')
    
# %%
tech = 'sas'
if tech == 'python':
    flag = 'Dobry wybór'
else:
    flag = 'Poszykaj czegos lepszego'
    
# %%
tech = 'python'
'dobry wybór' if tech == 'python' else 'poszukaj czegos lepszego'

# %%
text = 'jklsdfjlsdfjlksdjfsdljkdsiojuqmfdjklljskl'
'Zawiera' if text.find('q') else 'Nie zawiera'

# %%
text = 'jklsdfjlsdfjlksdjfsdljkdsiojuqmfdjklljskl'
if 'q' in text:
    print('Zawiera')
else:
    print('Nie zawiera')    

# -*- coding: utf-8 -*-

i = 0
while i <= 5:
    print(i)
    i += 1
    
# %%
n = 0
while True:
    print(n)
    if n >= 10:
        break
    n += 1

# %%
while True:
    name = input('podaj swoje imie: ')
    if len(name) >= 3 and name.isalpha():
        break
    else:
        print('imie musi zawierać minimum 3 znaki i nie może zawierać cyfr')
print('Czesc {}'.format(name))

# %%
n = 0
while n < 20:
    n +=1
    if n % 2 == 0:
        continue
    print(n)
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = int(input('wprowadź szukaną wartosc: '))
idx = 0

while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('znaleziono element {} na pozycji {}.'.format(wartosc, idx + 1))
else:
    print('nie znaleziono szulanej wartosci')

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = int(input('wprowadź szukaną wartosc: '))
idx = 0

while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)
# %%
num = [23, 12, 53, 13, 65, 1, 45]
idx = 0
wartosc = 13
f = False

while idx < len(num):
    if num[idx] == wartosc:
        f = True
        break
    idx += 1
if f:
    print('Znaleziono')
else:
    print('Nie znaleziono')

# %% 
KOD_PIN = '0000'
pin = input('podaj kod pin: ')

while pin != KOD_PIN:
    pin = input('błędny kod, spróbuj jeszcze raz: ')
    
print('Zalogowany')

# %%
KOD_PIN = '0000'
pin = ''
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input('wprowadz kod pin: ')
    if pin == KOD_PIN:
        print('Zalogowany')
        break
    counter += 1
else:
    print('Zbyt dużo prób logowania.')

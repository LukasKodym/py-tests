# -*- coding: utf-8 -*-


# %%
print(2 + 2)

# %%
print(3 * 3)

# %%
print(2 + 2 * 2)
print(4 - 2 * 2)

# %%
10 / 3
4 / 2

# %%
print(10 // 3)
print(10 % 3)

# %%
2 ** 5

# %%
a = 10
b = 20
c = a * b
print(c)

# %%
print('love python')
print("love python")

# %%
print("it's the best")
print('it\'s the best')

# %%
print("""python
3.8""")

print('python\n3.8')

# %%
print('\tPython')
print('\t\t\tPython')

# %%

print('C:\path\to\something\new')
print('C:\\path\\to\\something\\new') #recomended option
print(r'C:\path\to\something\new')

# %%
import os
os.getcwd()

# %%
text = 'I love Python. '
print(text)
print(text * 5)
# %%
'Python'
'Py' 'thon'
print('Py' 'thon')

# %%
url = 'https://docs.google.com/document/d/1l16PpOEVONT_4OKHVonQimOivu8xZKxy_m5c2cA67UE/edit?ts=5c001269'

url_2 =('https://docs.google.com/document/d/1l16PpOEVONT_4OKHVonQimOivu8xZKxy_'
        'm5c2cA67UE/edit?ts=5c001269')
# %%
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')

# %%
age = 27
imie = 'Paweł'

print(imie + ' ' + str(age))
print(imie, age)
print('{} ma {} lat'.format(imie, age))
print('{0} ma {1} lat'.format(imie, age))
print('{1} ma {0} lat'.format(imie, age))

# %%
saldo = 40
saldo += 30
print(saldo)
saldo -=10
print(saldo)
# %%
lokata = 1000
czynnik_ukumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_ukumulacyjny
print('wartoć lokaty po roku:', lokata_po_roku)

# %%
pixel = 150
# pixel = pixel / 255
pixel /= 255
print(pixel)

# %%
base = 2
base **= 5
print(base)

# %%
x = 103
x %= 10
print(x)

# %%
imie = 'Paweł '
nazwisko = 'Krakowiak'
imie += nazwisko
print(imie)

# %%
name = 'Python '
version = '3.7'
name += version

print(name)
# %%
kwota_poczatkowa = 1000
stopa_procentowa = 0.05
okres_trwania = 2

wartosc = kwota_poczatkowa * (1 + stopa_procentowa)**okres_trwania







 









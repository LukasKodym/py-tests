# -*- coding: utf-8 -*-
# %% zad 1
for i in range(5):
    print(i)

# %% zad 3
wynik = 0
for i in range(5):
    wynik += 6
    print(wynik)

# %% zad 4
# a = [0, 1, 3, 6, 10]
# for num in a:
#     print(num)

z = 0
for i in range(5):
    z += i
    print(z)

# %% zad 5
for i in range(53, 58):
    print(i)

# %% zad 6
for i in range(1, 8):
    if i == 5:
        print('Zanalazłem {}!'.format(i))
    print(i)

# %% zad 7
num = [1, 2, 3]
string = ['a', 'b', 'c']

for i in num:
    for j in string:
        print(i, j)

# %% zad 8
a = list(range(1,9))
print(a)

# %% zad 9
for x in a:
    if x >= 5:
        break
    print(x)

# %% zad 10
x = 4
while x < 19:
    if x % 2 == 0:
        print(x)
    x += 1

# %% zad 11
tab = ['A', 'B', 'C', 'D']
for i in len(tab):
    i += 1
    







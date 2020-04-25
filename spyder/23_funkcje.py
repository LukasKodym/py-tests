# -*- coding: utf-8 -*-

def funkcja_1():
    print('Pierwsza funkcja uruchomiona')


print(type(funkcja_1))
funkcja_1
a = funkcja_1
funkcja_1()
fun = funkcja_1()


# %%
def funkcja_2(x, y):
    print('podane argumenty to: {1} i {0}'.format(x, y))


funkcja_2(2, 6)
funkcja_2('4', 2)


# %%
def funkcja_3(x=3, y=10):
    print('podane argumenty to: {0} i {1}'.format(x, y))


funkcja_3()
funkcja_3(5)
funkcja_3(y=3, x=5)

# %%
import math

math.sqrt(9)
math.exp(1)
math.sin(0)


# %%
def add(x, y):
    return x + y


result = add(2, 6)


# %%
def subtract(x: int, y: int):
    """
    Subtracting two numbers

    Parameters
    ----------
    x : TYPE
        INTIGER.
    y : TYPE
        INTIGER.

    Returns
    -------
    Subtraction result.

    """
    return x - y


subtract(10, 5)


# %%
def print_menu():
    print('Start programu...')
    print('*' * 30)
    print("""Wybierz jedną z podanych opcji:
          0 - logowanie
          1 - wyjscie""")
    print('*' * 30)
    print('Koniec programu.')


print_menu()


# %%
def print_even(maximum):
    even = []
    for i in range(maximum + 1):
        if i % 2 == 0:
            even.append(i)
    return even


# print_even(10)
num = print_even(20)


# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)


write_file('sample_3.txt', 'Pierwsza linia.\nDruga linia.')
write_file('sample_4.txt', 'Pierwsza. \nDruga. \nTrzecia.')


# %%
def calculate_profit(pv=1000, rate=0.03, n=1):
    return pv * (1 + rate) ** n - pv


# calculate_profit(1000, 0.2, 15)
calculate_profit()


# %%
def drukuj_nieparzyste(maksimum=20):
    odd = []
    for i in range(maksimum + 1):
        if i % 2 != 0:
            odd.append(i)
    return odd


a = drukuj_nieparzyste()
print(a)

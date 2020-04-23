# -*- coding: utf-8 -*-

def funkcja_1():
    print('Pierwsza funkcja uruchomiona')


print(type(funkcja_1))
funkcja_1
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

# -*- coding: utf-8 -*-

def test_args(x, *args):
    print('Piertwszy parametr: {}'.format(x))
    for arg in args:
        print('Kolejny parametr *args: {}'.format(arg))


test_args(1, 0, 2, 3, 4, 5)


# %%
##
def funkcja_1(x, y, *args):
    print('x = ', x)
    print('y = ', y)
    print('*args = ', args)


funkcja_1(2, 5)
funkcja_1(2, 5, 6)
funkcja_1(1, 2, 3, 4)


# %%
##
def suma(x, y):
    return x + y


def suma_n(*args):
    return sum(args)


# %%
##
suma(2, 3)
# suma(2, 3, 4)
suma_n(2, 3, 4)


# %%
##
def policz_srednia(*args):
    return sum(args) / len(args)


policz_srednia(2, 2, 3, 9)


# %%
##
def funkcja_2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)


funkcja_2(**{'a': 1, 'b': 2})

# funkcja_2(a=1, b=2)


# %%
##
def fun(**kwargs):
    print(kwargs)


fun(a=1, b=2)
fun(x1=10, x2=20, x3=30)


# %%
##
def fun_2(*args, **kwargs):
    print(args)
    print(kwargs)


fun_2(1, 2, 4, a=10, b=12)


# %%
##
def fun_3(*args, **kwargs):
    print(sum(args))
    print(kwargs.values())


fun_3(1, 2, 4, a=10, b=12)


# %%
##
def policz_kwargs(*args, **kwargs):
    return len(kwargs)


policz_kwargs(10, a=1, b=2)
policz_kwargs(a=1, b=2, c=3)

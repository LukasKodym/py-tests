# %%
##
def fn():
    print('Witaj!')


fn()


# %%
##
def fn(a=0, b=0):
    print(a + b)


fn()
fn(3, 4)


# %%
##
def fn(a, b, c):
    print(a + b + c)


fn(2, 4, 4)


# %%
##
def fn(a, b=0, c=0):
    print('a:', a, 'b:', b, 'c:', c)


fn(2, c=5)
fn(2, c=1, b=7)
fn(b=2, a=4, c=0)
fn(2, 5, 7)


# %%
##
def fn(a, *args, **dict_args):
    print(a)
    # print(args)
    # print(dict_args)
    for arg in args:
        print(arg)
    for key in dict_args:
        print(dict_args[key])


fn(3, 1, 4, 5, 'cs', True, user='admin', version=2.5)


# %%
##
def fn(a, b):
    return a + b, a * b, a - b


r = fn(2, 4)
print(r)

# -*- coding: utf-8 -*-

# %%
##
print(abs(10))
print(abs(-10))

# %%
##
bool([])
bool('')
bool({})
bool(' ')
bool(True)
bool(0)
bool(12)

# %%
##
dir(list)
dir(tuple)

# %%
##
enumerate(['sas', 'python', 'java'])
list(enumerate(['sas', 'python', 'java']))

# %%
##
eval('1 + 1')

x = 10
eval('x + 13')

# %%
##
# filter?
filter(abs, [-2, -1, 0, 1, 2])
list(filter(abs, [-2, -1, 0, 1, 2]))

# %%
##
list(filter(bool, ['python', '', 'java']))

# %%
##
float(1)
float(1.0)
float('1')
float('3.5')

# float('aaaa') # expected error

# %%
##
type(1)
type('fgh')

# %%
##
# help()
help(float)
help(int)

# %%
##
isinstance(1, int)
isinstance(1.0, float)
isinstance('', str)

# %%
##
len('python')
len('')
len(' ')
len([])
len([[3, 4], [4, 5, 6, [1, 2]]])

# %%
##
x = list
print(type(x))
# print(len(x))

c = list()
print(type(c))

list('python')
list(range(10))

# %%
##
map(abs, [-2, -1, 0, 1, 2])
list(map(abs, [-2, -1, 0, 1, 2]))

# %%
##
names = ['pawel', 'tomek', 'adam']
list(map(str.title, names))

# %%
##
max([1, 3, 5, 9])
max('pawel')
max('tomek')

min([1, 3, 5, 9])
min('pawel')
min('tomek')

# %%
##
pow(2, 4)
2 ** 4

# %%
##
reversed([5, 3, 7])
list(reversed([5, 3, 7]))
list(reversed('python'))

# %%
##
round(4.1234867645, 2)

# %%
##
str(1)
str(1.5)

# %%
##
sum([3, 4, 5, 6])

# %%
##
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6, 8]

zip(lista_1, lista_2)
list(zip(lista_1, lista_2))

# %%
##
list(zip('python', 'course'))

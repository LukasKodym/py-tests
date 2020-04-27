# -*- coding: utf-8 -*-

# %%
##
for i in 'python':
    print(i)

# %%
##
name = 'python'

index = 0

for char in name:
    print(index, char)
    index += 1

# %%
##
for index in range(10):
    print(index)

# %%
##
for index in range(len(name)):
    print('nr indeksu: ', index, 'litera: ', name[index])

# %%
##
for i in enumerate(name):
    print(i)

# %%
##
for index, char in enumerate(name):
    print('nr indeksu: ', index, 'litera: ', char)

# %%
##
for i in [4, 5, 6, 8, 6]:
    print(i)

# %%
##
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)

# %%
##
for i in range(10, 20, 2):
    print(i)

# %%
##
for i in range(10, 0, -1):
    print(i)

# %%
##
string = 'Python Course'
for char in string[::-1]:
    print(char)

# %%
##
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

# %%
##
for char in zip('abcde', '12345'):
    print(char)

# %%
##
for char, num in zip('abcde', '12345'):
    print(char, num)

# %%
##
hashtags = '#sport#gym#fitness#'

result = ''
for char in hashtags:
    if char not in '#':
        result += char
    else:
        print(result)
        result = ''

# %%
##
hashtags = '#weekend#good#time#'
result = ''

for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        if result:
            print(result)
            result = ''

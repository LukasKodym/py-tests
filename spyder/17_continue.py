# -*- coding: utf-8 -*-

# %%
##
for i in range(10):
    if i == 6:
        continue
    print(i)

# %%
##
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

# %%
##
for i in range(20):
    if i % 2 == 1:
        continue
    print(i)

# %%
##
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)

# %%
##
hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result += char
print(result)

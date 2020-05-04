# -*- coding: utf-8 -*-

# %%
##
results = []

for i in range(100):
    results.append(i ** 2)
print(results)

# %%
##
results_2 = [i ** 2 for i in range(100)]

# %%
##
lista = [i for i in range(100)]

# %%
##
results = []
for i in range(100):
    if i % 5 == 0:
        results.append(i ** 2)

# %%
##
results_3 = [i ** 2 for i in range(100) if i % 5 == 0]

# %%
##
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

results_4 = []

for letter in letters:
    for num in numbers:
        results_4.append(letter + str(num))

# %%
##
results_5 = [letter + str(num) for letter in letters for num in numbers]

# %%
##
ls_1 = ['a', 'b', 'c']
ls_2 = ['a', 'b', 'c']

results_6 = [l_1 + l_2 for l_1 in ls_1 for l_2 in ls_2 if l_1 != l_2]

# %%
##
[[j for j in range(10)] for i in range(10)]

# %%
##
[[(i, j) for j in range(4)] for i in range(3)]

# %%
##
[[i * j for j in range(10)] for i in range(10)]

# %%
##
[[l1 + l2 for l2 in 'abcde'] for l1 in '12345']


# %%
##
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


[silnia(i) for i in range(10)]

# %%
##
print([i for i in range(30) if i % 4 == 0])

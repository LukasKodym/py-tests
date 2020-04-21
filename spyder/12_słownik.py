# -*- coding: utf-8 -*-

empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))

# e = set()

# %% metody tworzenia pustych struktur danych w Python

a = ()
b = []
c = {}

e = set()
f = tuple()
g = dict()
h = list()

# %%
pol_to_eng = {'jeden': 'one', 'dwa': 'two', 'trzy': 'three'}

name_to_digit = {'jeden': 1, 'dwa': 2, 'trzy': 3}

# %%
index_to_digit = {0: 1, 1: 2, 2: 3}

len(index_to_digit)

# %%
pol_to_eng['cztery'] = 'four'

# %%
pol_to_eng.clear()

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %%
pol_to_eng.keys()
# list(pol_to_eng.keys())

# %%
pol_to_eng.values()
# list(pol_to_eng.values())

# %%
pol_to_eng.items()
# list(pol_to_eng.items())

# %%
pol_to_eng['jeden']

# %%
pol_to_eng.get('jeden', 'NaN')
pol_to_eng.get('zero', 'NaN')

# %%
pol_to_eng.pop('dwa')
pol_to_eng.popitem()

# %%
pol_to_eng.update({'jeden': 1})

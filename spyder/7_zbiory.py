# -*- coding: utf-8 -*-


empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'c++', 'sql'}
print(techs)
print(type(techs))
print(len(techs))

# %%
set('python')
set('aaaaaeeeeellllll')

# %%
'python' in techs
'go' in techs

# %%
print(dir(set()))

# %%
techs.add('sas')
print(techs)

# %%
techs.remove('sas')
print(techs)

# %%
techs.pop() # wyswietla i usuwa dowolny element ze zbioru

# %%
techs.clear()
print(techs)

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A) # czy C jest podzbiorem A
C.issubset({5, 7})
A.issuperset(C) # czy A jest nadzbiorem C

A.union(B) # suma wszystkich elementów
A.intersection(B) # czesc wspolna
A.symmetric_difference(B) # pokazuje unikalne elementy dwóch zbiorów

D = A.copy()

# %%
x = 'Programowanie w języku Python - od A do Z'
new_set = set(x.lower().replace('-', '').replace(' ', '').replace('ę', 'e'))
print(len(new_set))

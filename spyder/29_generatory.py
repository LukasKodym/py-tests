# -*- coding: utf-8 -*-

# %%
##
def generator():
    
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    
    
# %%
##
gen = generator()

# %%
##
next(gen)

# %%
##
def generator_2(word):
    letters = list(word)
    for letter in letters:
        yield letter
    
gen_2 = generator_2('Python')

# %%
##
next(gen_2)

# %%
##
for item in generator_2('predator'):
    print(item)

# %%
##
files = ['scrypt_1.py', 'script_2.py', 'text.txt']

def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen_3 = gen_files(files)

# %%
##
next(gen_3)

# %%
##
for i in gen_3:
    print(i)

















import sys

print(dir(sys))
print(sys.version)
print(sys.platform)

# %%
import random

print(dir(random))
print(random.randint(2, 19))

# %%
from random import randint
from sys import version

print(randint(3, 9))
print(version)

# %%
import my_module

msg = my_module.my_function('Łukasz')
print(msg)
print(my_module.x)

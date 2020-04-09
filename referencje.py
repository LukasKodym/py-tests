a = 1
print(id(a))
a = 2
print(id(a))
a = 1
print(id(a))
print(dir(a))

def fn():
    return 2

print(fn())
print(fn)
print(dir(fn))

a = fn
print(a)
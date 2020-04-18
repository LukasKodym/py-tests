# %%
values = (1, 2, 3, 'abc', True)
print(values)
for i in values:
    print(i)
values[2] = 50 # error
print(values[2])

# %%
values = (1, 2, 3, 4, 5, 6, 7)
new_values = values[:3]
print(2 in new_values)
print(2 not in new_values)
print(len(new_values * 2 + (10, 20, 30)))
v = new_values * 2 + (10, 20, 30)
print(v)

# %%
values = (1, 2, 3, 4, 5, 6, 7)
print(values)
print(type(values))
my_list = list(values)
print(my_list)
print(type(my_list))

# %%
my_list = [10, 4, 5, 17, 7, 2, 5]
my_tuple = tuple(my_list)
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))
a = my_tuple[0]
print(a)
a, b, c, d, e, f, g = my_tuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

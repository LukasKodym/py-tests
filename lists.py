# %%
my_list = [1, 2, 3.5, 's', True]
my_list[4] = 20
print(my_list)

# %%
my_list = [10, 20, 30, 40]
for v in my_list:
    print(v)

# %%
my_list = [10, 20, 30, 40]
# my_list[4]
my_list.append(5)
my_list.append(3)
my_list.append(45)
my_list.append(77)
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)

# %%
my_list = [10, 20, 30, 40]
# print(my_list[0:2])
my_list_2 = [50, 60]
main_list = my_list + my_list_2 * 2
print(len(main_list))
print(10 in main_list)
print(10 not in main_list)

# %%
my_list = [i for i in range(10, 40, 5) if i % 2 == 0]
print(my_list)
my_list_2 = [[2, 4, 6], [1, 3, 5], [8, 5, 2]]
print(my_list_2)

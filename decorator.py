# %%
def my_decorator(fn):
    def wraper():
        print('przed dekorowaniem')
        fn()
        print('po dekorowaniu')
    return wraper

@my_decorator
def get_5_values():
    for v in range(1, 6):
        print(v)
get_5_values()

# %%
get_5_values_decorated = my_decorator(get_5_values)
get_5_values_decorated()
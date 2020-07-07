"""
Sum all the numbers of the array (in F# and Haskell you get a list)
except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge,
even if there are more than one with the same value!)
"""


# %%
##


def sum_array(arr):
    res = 0
    if arr is None:
        return 0
    elif len(arr) <= 2:
        return 0
    else:
        foo = sorted(arr)
        for item in foo[1:-1]:
            res += item
        return res


# or
#     return 0 if arr == None else sum(sorted(arr)[1:-1])


sum_array([-6, 20, -1, 10, -12])

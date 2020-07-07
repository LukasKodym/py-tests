"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
"""


# %%
##

def sum_mix(arr):
    for idx, item in enumerate(arr):
        if type(arr[idx]) is str:
            arr[idx] = int(item)
    return sum(arr)


sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])

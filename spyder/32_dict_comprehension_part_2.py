# -*- coding: utf-8 -*-

# %%
##
stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}

# %%
##
{key: 'Corp' if 'Corp' in val else 'Inc' for (key, val) in stocks.items()}

# %%
##
numbers = range(20)
numbers_dict = dict()

for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2

print(numbers_dict)

# %%
##
num_dict = {key: key ** 2 for key in range(20) if key % 2 == 0}

# %%
##
nested_dict = {'001': {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

for key, val in nested_dict.items():
    print(key, val)

# %%
##
{key: val['price'] for (key, val) in nested_dict.items()}

# %%
##
nested_dict_2 = {'001': {'price': 100, 'items': 4},
                 '002': {'price': 40, 'items': 9},
                 '003': {'price': 60, 'items': 8}}

# %%
##
for key, val in nested_dict_2.items():
    print(key, val)

# %%
##
{key: val['price'] for (key, val) in nested_dict_2.items()}

# %%
##
{key: val['price'] * val['items'] for (key, val) in nested_dict_2.items()}

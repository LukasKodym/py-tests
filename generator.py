def num_generator(end):
    n = 1
    nums = []
    while n <= end:
        nums.append(n)
        n += 1
    return nums

value = num_generator(1000)
print(value)

def num_generator(end):
    n = 1
    while n <= end:
        yield n
        n += 1

value = num_generator(100)
print(next(value))
print('coś innego')
print(next(value))
print(next(value))
print('coś innego')

for v in value:
    print(v)
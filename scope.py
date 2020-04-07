x = 1
def fn():
    # x = 2
    global x
    x += 1
    y = 3
    print(x, y)
fn()
print(x)
# print(y)
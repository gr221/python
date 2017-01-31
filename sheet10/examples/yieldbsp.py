
def func():
    i = 1.0
    while i < 10.0:
        i = i + 0.3
        yield i


it = func()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

print('------------------')
for var in func():
    print(var)


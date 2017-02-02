
import time
import multiprocessing as m

def fun(a,b,c):
    time.sleep(a)
    print('inside', b)
    time.sleep(c)
    return b

#def funx(tup):
#    return fun(*tup)


p = m.Pool(5)

r1 = p.apply_async(fun, (5, "fuenf", 2))
r2 = p.apply_async(fun, (7, "drei", 3))

print("applied!")

for r in (r1,r2):
    print('Result:', r.get())

print("done")
print()

#ri = p.map_async(funx, [
#    [1, "eins", 1], [4, "vier", 4], [3, "drei", 3],
#    [8, 'acht', 8], [9, "neun", 9], [10, 'zehn', 10],
#    [2, 'zwei', 2] ] )
#
#print('imapped!')
#print('imapped results:', ri.get())



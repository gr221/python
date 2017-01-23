f = open("pibin.txt", "rb")
data = f.read()
f.close()

from array import *

binaer = array('f')
binaer.frombytes(data)
for b in binaer:
    print(b)

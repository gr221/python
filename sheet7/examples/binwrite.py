from math import *
from array import *

f = open("pi.txt", "w")
print(pi, file=f)
f.flush()
f.close()

binaer = array('d') # "double": Zahlen mit
# Nachkommastellen doppelter Genauigkeit
binaer.fromlist( [pi] )

g = open("pibin.txt", "wb")
g.write(binaer.tobytes())
g.flush()
g.close()

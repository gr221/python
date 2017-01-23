import pylab as pl
import random

data = [ ]
yy = [ ]
for i in range(0,1000):
    #data.append(random.uniform(0,10))
    data.append(random.gauss(5,2))
    yy.append(0)

pl.hist(data)
pl.plot(data,yy,'r*')
pl.show()


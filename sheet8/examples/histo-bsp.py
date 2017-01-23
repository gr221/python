import pylab as pl
import random
random.seed(1001)
pl.title("Histogram")
data = [ ]
yy = [ ]
for i in range(0,30):
    data.append(random.uniform(0,10))
    yy.append(random.uniform(0.1,0.9))

pl.hist(data, range=(0,10), bins=10, color='yellow')
pl.plot(data,yy,'ro', markersize=10)
pl.show()


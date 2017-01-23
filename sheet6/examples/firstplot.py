import pylab as pl
import math

xx = [ ]
yy = [ ]
for i in range(0,101):
    xx.append(i * 0.1)
    yy.append(math.sin(i * 0.1) )

pl.plot(xx, yy, 'r*-')
#print(xx)
#print(yy)

x = pl.linspace(0,10,101)
y = 1.5*pl.cos(2*x) # das ist NICHT math.cos
y[50] = 2.0
pl.plot(x,y,'b:')

#print(x)
#print(y)

pl.show()

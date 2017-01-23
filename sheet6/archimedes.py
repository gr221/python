import pylab as pl
import math

values = pl.linspace(0, 4*math.pi, 1000)
x = values*pl.cos(values)
y = values*pl.sin(values)


x_1 = values*pl.cos(values) 
y_1 = values*pl.sin(values)

pl.plot(x,y,'g')
pl.plot(x_1,y_1,'r')
pl.show()


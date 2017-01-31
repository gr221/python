from pylab import *
r = 5
x = linspace(-r,r,1000)
plot(x,cosh(x),'b-')
y0 = cosh(0)
A  = (cosh(r)-cosh(0))/r**2
plot(x,A*x**2+y0,'r-')
show()

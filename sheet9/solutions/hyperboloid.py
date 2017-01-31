from pylab import *
from mpl_toolkits.mplot3d import Axes3D

x = linspace(-1,1,201)
y = linspace(-1,1,201)
X,Y = meshgrid(x,y)

f = figure()
ax = f.add_subplot(111,projection='3d')
ax.set_aspect('equal')

Z = X*X - Y*Y   # Z = Z(X,Y)

ax.plot_surface(X,Y,Z,color='yellow')
show()

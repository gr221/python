from pylab import *
from mpl_toolkits.mplot3d import Axes3D

#x = linspace(-15,15,201)
#y = linspace(-15,15,201)
#X,Y = meshgrid(x,y)
#X,Y = mgrid[ -15:15:201j, -15:15:201j ]
X,Y = mgrid[ -15:15:0.1,  -15:15:0.1 ]

f = figure()
ax = f.add_subplot(111,projection='3d')
ax.set_aspect('equal')
ax.plot( [0],[0],[15], 'w') # unsichtbarer punkt,
                            # wegen Achsenskalierung

Z = cos(sqrt(X*X + Y*Y))    # Z = Z(X,Y)
#for i in range(0,201):
#    for j in range(0,201):
#        Z[i,j] = cos(sqrt(X[i,j]*X[i,j] + Y[i,j]*Y[i,j]))

ax.plot_surface(X,Y,Z,color='yellow')
show()

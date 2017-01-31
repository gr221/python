import mayavi.mlab as ml
import numpy as n

t = n.linspace(0,2*n.pi,20)
x = n.sin(t)
y = n.cos(t)
z = n.ones_like(t)

ml.plot3d(x,y,z, t )
#ml.points3d(x,y,z,t)

ml.show()


import numpy as np
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import sys

u_ = np.linspace(0,2.0*np.pi,20)
v_ = np.linspace(0,4,10)

U,V = np.meshgrid(u_, v_)
u = U.flatten()
v = V.flatten()

#------- Koordinatentranformation ------
#        Das 'biegt' die Flaeche in
#        eine dreidimensionale Form
#        
x = np.cos(u)
y = np.sin(u)
z = v
#---------------------------------------

tr = mtri.Triangulation(u, v)
fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x,y,z, triangles=tr.triangles, color='yellow' )
pl.show()

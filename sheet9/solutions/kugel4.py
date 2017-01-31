from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import random

phi1 = linspace(0,2*pi,10)
theta1 = linspace(0,pi, 10)

PHI,THETA = np.meshgrid(phi1,theta1)

phi = PHI.flatten()
theta = THETA.flatten()

tr = mtri.Triangulation(phi,theta)

x = 5 * np.cos(phi) * np.sin(theta)
y = 5 * np.sin(phi) * np.sin(theta)
z = 5 *    1        * np.cos(theta)

fig = figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

print(tr.triangles)

ax.set_xlim3d(-7,7)
ax.set_ylim3d(-7,7)
ax.set_zlim3d(-7,7)

ax.set_aspect('equal')
ax.plot_trisurf(x,y,z, triangles=tr.triangles,
        color=(1,0,0,0.8), edgecolor=(0,0,0,0.2) )

show()

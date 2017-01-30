import numpy as np
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import sys

u_ = np.linspace(0,2.0*np.pi,20)
v_ = np.linspace(0,4,20)

U,V = np.meshgrid(u_, v_)
u = U.flatten()
v = V.flatten()

x = np.cos(u)
y = np.sin(u)
z = v

tr = mtri.Triangulation(u, v)
#print(tr.triangles)

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x,y,z, color='yellow', triangles=tr.triangles )

pl.show()
sys.exit(0)

# u, v are parameterisation variables
u = (np.linspace(0, 2.0 * np.pi, endpoint=True, num=50) * np.ones((10, 1))).flatten()
v = np.repeat(np.linspace(-0.5, 0.5, endpoint=True, num=10), repeats=50).flatten()

# This is the Mobius mapping, taking a u, v pair and returning an x, y, z
# triple
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)

# Triangulate parameter space to determine the triangles
tri = mtri.Triangulation(u, v)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# The triangles in parameter space determine which x, y, z points are
# connected by an edge
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)

pl.show()

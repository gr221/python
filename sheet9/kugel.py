import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D

n_angles = 20
theta = np.linspace(0, np.pi, n_angles)
phi = np.linspace(0, 2*np.pi, n_angles)

theta, phi = np.meshgrid(theta, phi)
theta = theta.flatten()
phi = phi.flatten()


X = np.sin(theta)*np.cos(phi)
Y = np.sin(theta)*np.sin(phi)
Z = np.cos(theta)
tr = mtri.Triangulation(X,Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(X,Y,Z, triangles = tr.triangles)
plt.show()

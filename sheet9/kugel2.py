import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import sys

n_angles = 20
phi_ = np.linspace(0,2.0*np.pi, n_angles)
theta_ = np.linspace(0,np.pi , n_angles/2)

Phi, Theta = np.meshgrid(phi_, theta_)
phi = Phi.flatten()
theta = Theta.flatten()

x = np.cos(phi)*np.sin(theta)
y = np.sin(phi)*np.sin(theta)
z = np.cos(theta)

tr = mtri.Triangulation(phi, theta)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x,y,z, triangles=tr.triangles)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import mpl_toolkits.mplot3d as a3

l = 2
a = 1
s_h= np.sqrt(3)/2 *a
hgt = np.sqrt(2)/2 *a
vertices = [
        [ [l-s_h,0,0], [0,l-s_h,0], [0,0,-l + hgt] ],
        [ [l-s_h,0,0], [0,-l+s_h,0],[0,0,-l + hgt] ],
        [ [-l+s_h,0,0], [0,-l+s_h,0], [0,0,-l+hgt] ],
        [ [-l+s_h,0,0], [0,l-s_h,0], [0,0,-l+hgt] ],
        [ [l-s_h,0,0], [0,l-s_h,0], [0,0,l-hgt] ],
        [ [l-s_h,0,0], [0,-l+s_h,0],[0,0,l-hgt] ],
        [ [-l+s_h,0,0], [0,-l+s_h,0], [0,0,l-hgt] ],
        [ [-l+s_h,0,0], [0,l-s_h,0], [0,0,l-hgt] ]
        ]

fcol = ['red']


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_aspect('equal')
ax.add_collection3d(a3.art3d.Poly3DCollection(
    vertices,
    facecolors=fcol))
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

plt.show()

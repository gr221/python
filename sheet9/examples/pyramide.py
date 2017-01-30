import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import random
import mpl_toolkits.mplot3d as a3


vertices = [
        [ [0,0,0], [1,0,0], [0,1,0] ],
        [ [0,0,0], [1,0,0], [0,0,1] ],
        [ [0,0,0], [0,0,1], [0,1,0] ],
        [ [0,0,1], [0,1,0], [1,0,0] ]   ]

fcol = [ 'blue', 'red', 'green', 'yellow' ]
ecol = [ 'black', 'white', 'black', 'white' ]

fig = pl.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.set_aspect('equal')
ax.add_collection3d(a3.art3d.Poly3DCollection(\
        vertices,
        facecolors=fcol,
        edgecolors=ecol))

pl.show()

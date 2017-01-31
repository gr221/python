import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import random
import mpl_toolkits.mplot3d as a3

s2 = np.sqrt(2)
hi = np.sqrt(1 - (s2/2)**2)*6

vertices = [ ]

hexagon = [ [3,-1,0],[3,1,0],
            [2,2,hi/3],[1,1,hi*2/3],
            [1,-1,hi*2/3],[2,-2,hi/3] ]
quadrat = [ [1,1,hi*2/3], [-1,1,hi*2/3],
            [-1,-1,hi*2/3], [1,-1,hi*2/3] ]
seite = [ [3,1,0], [2,2,hi/3],
          [1,3,0], [2,2,-hi/3] ]

fcol = [ ]
ecol = (0,0,0)

def flip_z(vertices):
    retval = [ ]
    for vertex in vertices:
        retval.append( [vertex[0],vertex[1],-vertex[2]] )
    return retval

def rot_z(vertices):
    # x --> y
    # y --> -x
    retval = [ ]
    for vertex in vertices:
        retval.append( [-vertex[1],vertex[0],vertex[2]] )
    return retval

tblue = (0,0,1,0.5)
tred =  (1,0,1,0.5)
black = (0,0,0)

def vertexshift(x,y,z,vertices):
    retval = [ ]
    for vertex in vertices:
        retval.append( [
            vertex[0]+x,
            vertex[1]+y,
            vertex[2]+z ] )
    return retval

def appokt(x,y,z,face):
    global vertices, fcol
    h = hexagon
    u = flip_z(hexagon)
    for n in range(0,4):
        vertices.append(vertexshift(x,y,z,h))
        vertices.append(vertexshift(x,y,z,u))
        h = rot_z(h)
        u = rot_z(u)
    vertices.append(vertexshift(x,y,z,quadrat))
    vertices.append(vertexshift(x,y,z,flip_z(quadrat)))
    s = seite
    for n in range(0,4):
        vertices.append(vertexshift(x,y,z,s))
        s = rot_z(s)
    for i in range(0,14):
        fcol.append(face)

appokt(0,0,0,'blue')
appokt(0,0,hi*2*2/3,'blue')
appokt(0,0,-hi*2*2/3,'blue')
appokt(4,0,hi*2/3,'red')
appokt(4,0,-hi*2/3,'red')
appokt(4,0,3*hi*2/3,'red')
appokt(4,-4,0,'green')

fig = pl.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_xlim( (-13,13) )
ax.set_ylim( (-13,13) )
ax.set_zlim( (-13,13) )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_aspect('equal')
ax.add_collection3d(a3.art3d.Poly3DCollection(\
        vertices,
        facecolors=fcol,
        edgecolors=ecol))

pl.show()

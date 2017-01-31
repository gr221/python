import numpy as np
from numpy import array, random
from tvtk.api import tvtk
import mayavi
import mayavi.mlab as ml


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

points = [ ]
polys = [ ]
scalars = [ ]

j = 0
i = 0
for poly in vertices:
    p = [ ]
    for point in poly:
        points.append(point)
        p.append(j)
        j += 1
    polys.append(p)
    if fcol[i] == 'blue':
        scalars.append(0.1)
    elif fcol[i] == 'red':
        scalars.append(0.2)
    elif fcol[i] == 'green':
        scalars.append(0.3)
    else:
        scalars.append(0.4)
    i += 1




# The TVTK dataset.
mesh = tvtk.PolyData(points=points, polys=polys)
mesh.cell_data.scalars = scalars
mesh.cell_data.scalars.name = 'cell data'

ml.pipeline.surface(mesh,colormap='spring',opacity=0.5)
ml.show()

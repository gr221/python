import mayavi.mlab as ml
import numpy as n

T = n.linspace(0,2*n.pi,1700)

X = 2*T
Y = 3*T+1
Z = 4*T

src = ml.pipeline.line_source( X, Y, Z, n.log(T+1))
src2 = ml.pipeline.stripper(src)
src3 = ml.pipeline.tube(src2,tube_radius=2.0,tube_sides=20)
src4 = ml.pipeline.surface(src3,colormap='flag')
ml.show()


import mayavi.mlab as ml
import numpy as n

t = n.linspace(0,2*n.pi,200)
x = n.sin(t)
y = n.cos(t)
z = n.ones_like(t)

# genauso wie torus.py,
# aber jetzt in einzelne Piplines aufgeteilt,
# so dass man hier Parameter aender kann.

src = ml.pipeline.line_source(x,y,z,t)
src2 = ml.pipeline.stripper(src)
src3 = ml.pipeline.tube(src2,tube_radius=0.2,
        tube_sides=50)
src4 = ml.pipeline.surface(src3,colormap='flag')

# get current figure
f = ml.gcf()
# in Datei speichern
# f.scene.save("mein_torus.png")

ml.show()


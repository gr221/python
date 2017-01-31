import mayavi.mlab as ml
import numpy as n

t = n.linspace(0,2*n.pi,200)
x = n.sin(t)
y = n.cos(t)
z = n.ones_like(t)

src = ml.pipeline.line_source(x,y,z,t)
src2 = ml.pipeline.stripper(src)
src3 = ml.pipeline.tube(src2,tube_radius=0.2,
        tube_sides=50)
src4 = ml.pipeline.surface(src3,colormap='flag')

# Animation definieren. Der Dekorator "ml.animate" ist bereits  definiert.
@ml.animate(delay=1000)
def animiere(quelle):
    aenderung = 0.1
    grenze = 0.1
    while True:
        t = n.linspace(0, grenze,200)
        x = n.sin(t)
        y = n.cos(t)
        z = n.ones_like(t)
        grenze = grenze + aenderung
        if grenze > 2*n.pi:
            grenze = 0.1
        quelle.set(x=x,y=y,z=z,t=t)
        yield

# die Animation ausfuehren
ani = animiere(src.mlab_source)

ml.show()  ###   for  x in in ani:
           ###       .......


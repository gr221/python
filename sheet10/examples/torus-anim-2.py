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

@ml.animate(delay=30)
def animiere():
    az = 0
    el = 0
    es = 1
    ax = 1
    while True:
        ml.view(azimuth=az, elevation=el, distance=10)
        az += ax
        el += es
        if az > 350: az = -1
        if ax < 0: ax = 1
        if el > 90: es = -1
        if el <= 0: es = 1
        yield

@bla
def func():
    #.....
    pass

# ist das gleiche wie:

def func():
    #.... 
    pass
func = bla(func)


ani = animiere()

ml.show()


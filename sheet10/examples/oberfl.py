import mayavi.mlab as ml
import numpy as n

# Zeichne eine Oberflaeche (Funktionslandschaft).

# mgrid: grid in x-y-Ebene, jeweils von -5 bis +5,
# unterteils in 140 Schritte
X,Y = n.mgrid[-5:5:140j, -5:5:140j]

Z = n.sin((X**2 + Y**2)) * \
        n.exp(-(X**2 + Y**2)*0.1)

ml.surf(X, Y, Z)

ml.show()



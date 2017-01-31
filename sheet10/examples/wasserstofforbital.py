# 
# Wasserstoff-Orbitale
#
# Ein Beispiel fuer Iso-Flaechen mit mayavi.
# Hier wird eine skalare Dichte berechnet
# (hier die Wellenfunktion des Wasserstoffatoms)
# und gezeichnet werden Flaechen gleicher Dichte.
# 
import numpy as nu
import mayavi
import mayavi.mlab as ml
import sys
import scipy
import scipy.special
from scipy.special import sph_harm as Ylm

# Ein 3-d grid. X, Y und Z sind jeweils 3-dimensionale arrays
X,Y,Z = lat = nu.mgrid[-10:10:130j,-10:10:130j,-10:10:130j]

def spherical(x,y,z):
    """ Umrechnung der Cartesischen Koorinaten
        in spaerische Koordinaten (Kugelkkoordinaten)
    """
    radius = nu.sqrt(x**2 + y**2 + z**2)
    radi = nu.sqrt(x**2 + y**2)
    theta = nu.arctan2(z, radi)
    phi = nu.arctan2(y, x)
    return radius,phi,theta-0.5*nu.pi

def harmonic(x,y,z,l,m):
    """ Kugelflaechenfunktion.
    """
    r,f,t = spherical(x,y,z)
    a = Ylm(m,l,f,t)
    return nu.sign(a.real)

def orbital(x,y,z,l,m):
    """ Orbital. Kombination aus den
        Kugelflaechenfunktionen und 1/r.
    """
    r,f,t = spherical(x,y,z)
    a = Ylm(m,l,f,t)
    return (1.0/r) * a.real


fig = ml.figure()

# Das orbital wird die Quelle der darzustellenden Daten
# m ist die Art des Orbitals
#   m==0:  s-Orbital,
#   m==1:  p-Orbital,
#   m==2:  d-Orbital,
#   m==3:  f-Orbital
# l ist im Bereich 0..m und bezeichnet das Orbital.
# 

m = 2
l = 0
src = ml.pipeline.scalar_field(X,Y,Z,orbital(X,Y,Z,m,l))

# Iso-Flaechen. Es gibt zwei Isoflaechen.
src2 = ml.pipeline.iso_surface(src, contours=[-0.1, +0.1],
        colormap='jet', opacity=1.0,
        vmax=0.15, vmin=-0.15, reset_zoom=True)

print(ml.view())
# Blickwinkel einstellen
ml.view(azimuth=70, elevation=60, distance=20)
print(ml.view())
ml.show()

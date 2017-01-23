from pylab import *
import scipy.stats
import scipy.optimize

# Willkürliche Beispieldaten
x = [1,   2,   3,   4,   5,   6, 7]
y = [2.1, 3.9, 5.5, 9.1, 9.1, 11.1,    15.6]

# lineare Regression,
# sl:  Steigung der Geraden,
# it:  y-Achsenabschnitt der Geraden
sl,it,rv,pv,sterr = scipy.stats.linregress(x,y)

# x in ndarray umwandeln, dann plotten
xa = fromiter(x, dtype=float)
plot(xa, sl*xa+it, 'b-')

# Lineare funktion
def linear(x,a,c):
    return a*x +c

# Optimierung mit iterativer Methode
popt,pcov = scipy.optimize.curve_fit(
        linear, x, y, p0=(1,1) )
plot(xa, linear(xa, popt[0], popt[1]), 'g:')


def fun(x,A,B,C,D):
    return A*arctan(B*x +C) +D
popt,pcov = scipy.optimize.curve_fit(
        fun, x, y, p0=(1,1,1,1))
plot(xa, fun(xa,popt[0],popt[1],popt[2],popt[3]), 'k:')

plot(x,y,'r*')
show()

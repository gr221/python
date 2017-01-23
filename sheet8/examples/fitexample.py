import matplotlib
import sys
if len(sys.argv) == 2:
    matplotlib.use('pdf')

import scipy as sc
import scipy.optimize as opt
import scipy.odr as odr
import numpy as np
import pylab as pl
import random
import sys

random.seed(1)

#--------------------------------------------------------
#  generiere die „Messdaten“: Gaußkurve mit zufälligem
#  Rauschen darauf.
#
x = np.linspace(-2,2,41)
y = np.array( [0.7*np.exp(-(0.9*x[i]+0.2)**2)\
        + random.uniform(-0.1,0.1) \
        for  i in range(0,len(x)) ] )
s = np.array( [random.uniform(0,0.2)\
        for i in range(0,len(x)) ] )
z = np.array( [random.uniform(0,0.5)\
        for i in range(0,len(x)) ] )

print(len(x), x)
print(len(y), y)

#-----------------------------------------------------------
# zeichne die „Messdaten“ inklusive Fehlerbalken
pl.errorbar(x,y,yerr=s,xerr=z,fmt='r*-')

#------------------------------------------------------------
# Definiere die Modellfunktion als Graußfunktion mit drei Parametern:
#   - Amplitude A
#   - Breite  w 
#   - Verschiebung phi
#   
def fitfunc(x, A, phi, w):
    return A*np.exp(-(w*x+phi)**2)
#-------------------------------------------------------------

print("--------------------------------------------------")
#   curve_fit fittet in callabe mit der unabhängigen Variablen x
#   and die Daten y
param,cov = opt.curve_fit(fitfunc, x, y,
        p0=[1,1,1], sigma=s)
print("fitted parameters", param)
print("covariance", cov)
print("--------------------------------------------------")

pl.plot(x,fitfunc(x,param[0],param[1],param[2]), 'b-',
        linewidth=3)

print("--------------------------------------------------")
#  Die funktion leastsq optimiert immer auf auf Null,
#  wobei das Callable errfunc ein Array zurückgeben muss.
errfunc = lambda pr,x,y,s: (y-fitfunc(x,*pr))/s
optparam,covar,infodict,mesg,ier =\
        opt.leastsq(errfunc, [1,1,1], args=(x,y,s),\
        full_output=True)
print()
print('optparam', optparam)
print('mesg', mesg)
print("--------------------------------------------------")
pl.plot(x,fitfunc(x,*optparam),'y-', linewidth=2)

print("--------------------------------------------------")
#  Die Funktion fmin optimiert global auf Null, sprich
#  das Callable errfunc muss hier nur genau einen Wert
#  zurückgeben.
errfunc = lambda pr,x,y,s: sum( abs((y-fitfunc(x,*pr))/s ) )
optparam,covar,infodict,mesg,ier =\
        opt.fmin(errfunc, [1,1,1], args=(x,y,s),\
        full_output=True)
print()
print('optparam', optparam)
print('mesg', mesg)
print("--------------------------------------------------")
pl.plot(x,fitfunc(x,*optparam),'b-', linewidth=2)


print("--------------------------------------------------")
#  ODR funktioniert ähnlich wie curve_fit, jedoch
#  werden hier auch Daten mit Fehlern in der abhänigen Variablen
#  (die die Variable x) möglich.
#  
model = odr.Model(lambda Aphiw,x: fitfunc(x,*Aphiw)) #expand tuple
data = odr.RealData(x,y,sx=z, sy=s) # mit x-fehler
#data = odr.RealData(x,y,sy=s,sx=0.0001) # (fast) ohne x-fehler
#data = odr.RealData(x,y) ganz ohne Fehler
modr = odr.ODR(data,model,beta0=[1,1,1])
outr = modr.run()
print("beta", outr.beta)
print("fehler in beta", outr.sd_beta)
#
# Anmerkung:  der "Fehler in Beta" (also hier outr.sd_beta)
# sind die Quadratwurzeln aus den Diagonaleintraegen
# der Kovarianzmatrix: sd_beta[i] = sqrt(cov_veta[i,i])
#
# Wie findet man das heraus?
# 1) Quellcode von scipy ansehen,
# 2) ODR Manual lesen:
#    http://docs.scipy.org/doc/external/odrpack_guide.pdf
#
print("covariance")
print(outr.cov_beta)
print("--------------------------------------------------")

pl.plot(x,fitfunc(x,*outr.beta), 'c-')

if len(sys.argv) == 2:
    pl.savefig(sys.argv[1]+".pdf")
    pl.show()
    sys.exit(0)
else:
    pl.show()

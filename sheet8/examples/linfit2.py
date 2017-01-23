import pylab as pl
import scipy
import scipy.optimize as opt

V = pl.fromiter( [1, 2.2, 2.9, 4.1, 5.07],dtype='float' )
A = pl.fromiter( [0.1, 0.2, 0.31, 0.3890, 0.55], dtype='float' )

def strom(spannung,R,R0):
    return R*spannung + R0

param,cov = opt.curve_fit(\
        strom, V, A, p0=[1,1] )

print(param)

pl.plot(V,A,'r*')
pl.plot(V, strom(V, param[0], param[1]), 'b-')
pl.show()


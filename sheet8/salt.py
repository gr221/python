import pylab as pl
import scipy.stats
import scipy.optimize
import array

f = open("intersalt1.txt", "r")
data = f.readlines()
data.pop(0)
blood_pressure=[]
natrium=[]
for i in range(0,len(data)):
    tmp = data[i].split()
    blood_pressure.append(float(tmp[2]))
    natrium.append(float(tmp[3]))

blood_pressure_arr = pl.fromiter(blood_pressure, dtype=float)

#Lineare Regression, sl: steigung, it: y-Achsenabschnitt
sl,it,rv,pv,sterr = scipy.stats.linregress(blood_pressure_arr, natrium)
# pl.plot(blood_pressure_arr, sl*blood_pressure_arr+it, 'b-')
print("Regression sl: ", sl, "  it: ", it)

#Iterative Methode
def linear(x,a,c):
    return a*x +c
popt,pcov = scipy.optimize.curve_fit(linear, blood_pressure, natrium)
# pl.plot(blood_pressure_arr, linear(blood_pressure_arr, popt[0], popt[1]), 'g-')
print("Iterativ  popt[0]: ", popt[0], "  popt[1]: ", popt[1])

pl.plot(blood_pressure_arr, natrium, 'r*')
pl.show()



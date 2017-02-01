import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = open("gebirge.data", "r")
werte = f.readlines()
f.close()
# print(werte)
data = np.empty((1,0))
for i in range(0,len(werte)):
    tmp = werte[i].split()
    for j in range(0,len(tmp)):
        data=np.append(data, float(tmp[j]))

data = np.reshape(data, (34,55))


y = np.linspace(0,33,34)
x = np.linspace(0,54,55)
X,Y = np.meshgrid(x,y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,data,cstride=1, rstride=1, cmap='rainbow')

plt.show()

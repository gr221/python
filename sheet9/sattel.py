import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def hyperbolic_paraboloid(x,y):
    return x*x-y*y

X = np.linspace(-3,3,500)
Y = np.linspace(-3,3,500)
print(X)
X,Y = np.meshgrid(X,Y)
print(X)
Z = hyperbolic_paraboloid(X,Y)
print("Zett")
print(Z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z) 
#Warum funktioniert Axes3d.plot_surface(X,Y,Z) nicht?
plt.show()

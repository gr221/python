import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0,2*np.pi,1000)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z)

plt.show()

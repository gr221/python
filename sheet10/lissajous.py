import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0,2*np.pi,1000)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)
r = [ np.sin(7*t),np.sin(7*t),np.sin(5*t-2)]
# r = [[x],[y],[z]]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z,'r-')
ax.plot(r[0],r[1],r[2],'g-')

plt.show()

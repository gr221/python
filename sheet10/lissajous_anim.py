import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def update_line(num,  line):
    line
    return line


t = np.linspace(0,2*np.pi,100)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)

X,Y = np.meshgrid(x,y)

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
# r = [ [np.sin(7*t)],[np.sin(7*t)],[np.sin(5*t-2)]]

lines = ax.plot(x[0:1],y[0:1],z[0:1])
# lines = ax.plot(r[0][0:1],r[1][0:1],r[2][0:1])

line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs = (lines))

plt.show()

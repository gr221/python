import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def update_line(num, r, lines):
    for line, data in zip(lines, r):
        line.set_data(data[0:2][ :num])
        line.set_3d_properties(data[2,:num])
    return line


t = np.linspace(0,2*np.pi,100)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)

r =[x,y,z]

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
# r = [ [np.sin(7*t)],[np.sin(7*t)],[np.sin(5*t-2)]]

lines = [ax.plot(dat[0][0:1],dat[1][0:1],dat[2][0:1])[0]for dat in r]
# lines = ax.plot(r[0][0:1],r[1][0:1],r[2][0:1])

line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs = (r,lines))

plt.show()

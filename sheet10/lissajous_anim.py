import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def update_line(num, data, line):
    print(data[..., :num+1])
    line.set_data(data[:2, :num+1])
    line.set_3d_properties(data[2, :num+1])
    return line


t = np.linspace(0,2*np.pi,100)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)

r = np.empty([3,100])
r[0] = x
r[1] = y
r[2] = z
# print(r)
# r =[x,y,z]
# r = [ [np.sin(7*t)],[np.sin(7*t)],[np.sin(5*t-2)]]

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')

line = ax.plot([],[],'r-')
# print(line)
# print(type(line[0]))

line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs = (r,line[0]),blit=True)

plt.show()

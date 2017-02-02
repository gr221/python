
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
 
 
def update_line(num, data, line):
    print(data[..., :num])
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num]) 
    print(line)
    return line,
 
t = np.linspace(0,2*np.pi,1000)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)

data = np.empty([3,1000])
data[0] = x
data[1] = y
data[2] = z
fig1 = plt.figure()
ax = fig1.add_subplot(111,projection='3d')
 
lines = ax.plot([], [], 'r-')
print('xxxxx', lines)
print(type(lines[0]))
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 1000, fargs=(data, lines[0]),\
                                   interval=50, blit=True)
plt.show()

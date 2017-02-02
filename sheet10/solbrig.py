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
 
fig1 = plt.figure()
ax = fig1.add_subplot(111,projection='3d')
 
data = np.random.rand(3, 25)
lines = ax.plot([], [], 'r-')
print('xxxxx', lines)
print(type(lines[0]))
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, lines[0]),\
                                   interval=1000, blit=True)
plt.show()

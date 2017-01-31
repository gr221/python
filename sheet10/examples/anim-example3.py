import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    print(data[..., :num].shape)
    line.set_data(data[..., :num])
    print(line)
    return line,

fig1 = plt.figure()

data = np.random.rand(2, 25)
lines = plt.plot([], [], 'r-')
print(type(lines[0]))
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, lines[0]),\
                                   interval=1000, blit=True)
plt.show()


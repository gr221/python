
from pylab import *
import matplotlib.animation as ani

positions = zeros((2,20))

def animateDots(t, line):
    global positions
    for i in range(0,20):
        positions[0,i] = i
        positions[1,i] = sin(t/100*(i+10))
    line.set_data(positions)
    return line,

f = figure()
lines = plot([ ],[ ],'r*')
xlim(-1,21)
ylim(-1.2,1.2)
aobj = ani.FuncAnimation(f, animateDots, interval=25,\
        frames=2000,
        fargs=(lines[0],), repeat=False)
#aobj.save('pendulum.mp4',fps=25) # requires ffmpeg
show()

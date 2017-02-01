import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

t = np.linspace(0,2*np.pi,1000)
x = np.sin(7*t)
y = np.sin(11*t+3)
z = np.sin(5*t-2)

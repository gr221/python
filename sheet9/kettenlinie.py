import numpy as np
import matplotlib.pyplot as plt

def parabel(x):
    return 1.644*x*x+1


index = np.linspace(-4,4,100)
print(index)
plt.plot(index, parabel(index))
plt.plot(index, np.cosh(index), 'r-')
plt.show()

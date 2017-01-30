from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

n_radii = 8
n_angles = 36

radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# print(radii)
# print(angles)

angles = np.repeat(angles[...,np.newaxis], n_radii, axis=1)
# print(angles)
# print(radii*np.cos(angles))

x = np.append(0, (radii*np.cos(angles)))

print(x)

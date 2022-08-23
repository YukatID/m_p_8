import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

A = np.array([[1,2,3],[4,0,6],[7,8,9]])
B = np.array([12,2,1])
print("Решение системы:")
print(np.linalg.solve(A,B))
fig = figure()
ax = Axes3D(fig)
X = np.arange(-15, -5, 1)
Y = np.arange(-5, 5, 1)
X, Y = np.meshgrid(X,Y)
Z = (X+2*Y-12)/(-3)
Z2 = (4*X-2)/(-6)
Z3 = (7*X+8*Y-1)/(-9)
ax.plot_surface(X,Y,Z,color='cyan')
ax.plot_surface(X,Y,Z2,color='green')
ax.plot_surface(X,Y,Z3,color='yellow')
ax.scatter(-9.2, 0.9, 6.5, 'z', 50, 'red')
show()
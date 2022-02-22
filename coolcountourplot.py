import matplotlib.pyplot as plt
import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


xvalues= np.linspace(-3,3,num=10000)
yvalues= np.linspace(-5,5,num=10000)

def f(x,y):
    return np.exp(-x**2-(y**2)/2)*np.cos(4*x) + np.exp(-3*((x+0.5)**2)+(y**2)/2)

z=f(xvalues,yvalues)

ax.plot(xvalues,yvalues,z)
plt.show()

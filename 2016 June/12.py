import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4 -4*x**3 +3*x**2 +2*x-1

x = np.arange(-1,3,0.0001)
y=f(x)

plt.plot(x,y)
plt.show()

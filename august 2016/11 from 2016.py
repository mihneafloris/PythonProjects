import numpy as np
import random
import math
import matplotlib.pyplot as plt
def f(x):
    return (1+0.2*x)*(1+0.1*x)/((1+x)*((1+0.02*x)**2)*((1+0.01*x)**2))

x = np.logspace(-4,2,10000)*1j
y=f(x)

plt.plot(np.real(y),np.imag(y))
plt.show()
    

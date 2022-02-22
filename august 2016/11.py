import numpy as np
import matplotlib.pyplot as plt
x=np.logspace(-4,2,100000,endpoint=True)
x=x*1j
def f(x):
    return (1+0.2*x)*(1+0.1*x)/(1+x)*((1+0.02*x)**2)*((1+0.01*x)**2)

plt.plot(np.real(f(x)),np.imag(f(x)))
plt.show()

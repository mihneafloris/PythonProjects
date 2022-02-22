from numpy import *
from matplotlib.pyplot import *

def f(x):
    return sin(x)*(0.003*x**4-0.1*x**3+x*x+4*x+3)

def g(x):
    return -10.*arctan(x)

x = np.arange(-7.,7.0005,0.0005)

plot(x,f(x))
plot(x,g(x))
show()

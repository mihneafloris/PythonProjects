from numpy import *
from scipy.optimize import bisect
from matplotlib.pyplot import *

def f(x):
    return sin(x)*(0.003*x**4-0.1*x**3+x*x+4*x+3)

def g(x):
    return -10.*arctan(x)

def h(x):
    return f(x)-g(x)

x = np.arange(-7.,7.0005,0.0005)

plot(x,f(x))
plot(x,g(x))
show()


# extra: use scipy bisect!
guess = [-4.38, 0.0,3.64,5.96]
d = 0.2
for x in guess:
   print(bisect(h,x-d,x+d))

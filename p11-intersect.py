from numpy import *
from matplotlib import pyplot as plt
from scipy.optimize import bisect

# Define functions
def f(x):
    return exp(x)*(cos(x)+2)-4
def g(x):
    return sqrt(x*x*x-2*x*x+9)

# Define function h(x)= f(x) - g(x) for root finding:
# x for h(x)=0, is where f(x)=g(x)
def h(x):
    return f(x)-g(x)

# Plot
x = arange(-10,10,0.1)
plt.plot(x,f(x))
plt.plot(x,g(x))
plt.show()

# Based on plot, called bisect for interval [0.8,1.4]
xroot = bisect(h,0.8,1.4)

print("Intersection at: (",xroot,",",f(xroot),")")
print("Intersection at: (",round(xroot,4),",",round(f(xroot),4),")")


import math as m
import numpy as np
import matplotlib.pyplot as plt

xlist=[]
ylist=[]
zlist=[]
t=0
dt=0.001
x=0.0
y=3.0
z=-10.0
while t<1:
    dxdt=10*(y-x)
    dydt=28*x-y-x*z
    dzdt=x*y-8/3*z
    x=x+dxdt*0.001
    y=y+dydt*0.001
    z=z+dzdt*0.001
    t=t+dt
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)

print(xlist[-1],ylist[-1],zlist[-1])
plt.plot(xlist,ylist)
plt.axvline(x=5)
plt.show()

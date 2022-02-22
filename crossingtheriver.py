import numpy as np
from math import pi, sqrt
import matplotlib.pyplot as plt
import math as m
A=12 #m/s
V=10 #m/s
L=100 #m
velocity=[]
velocityx=[]
velocityy=[]
length=[]
phi=0
xpos=[]
ypos=[]
time=[]
dt=0.1
x=0
y=0
t=0
watervelocity=[]

    
"""def positions(x,y):
    vx=np.sin(phi)*V - waterv(y)
    x=x+vx*dt
    vy=np.cos(phi)*V
    y=y+vy*dt
    v=sqrt(vx**2+vy**2)
    phi=arctan(vx/vy)
    return x,y#,v,vx,vy"""

def waterv(y):
    v = A*np.sin((pi*y)/L)
    watervelocity.append(v)
    return v
"""def phi(y):
    if 2*y<L:
        phi=np.arcsin(2*y/L)
    else:
        phi=np.arccos(-(L-2*y)/L)
    return phi
    """
getwatervelocity=waterv(y)
vx=10*m.sin(0)
vy=10*m.cos(0)
while y<=L:
    #vx=positions(x,y)[3]
    #vy=positions(x,y)[4]
    #y=positions(x,y)[1]
    #x=positions(x,y)[0]
    #v=positions(x,y)[2]
    x+=vx*dt
    y+=vy*dt
    vx=m.sin(phi)*V - waterv(y)
    vy=max(m.cos(phi)*V,.00001)
    phi=np.arccos(x/L)
    
        
    t=t+dt
    xpos.append(x)
    ypos.append(y)
    #time.append(t)
    #velocity.append(v)
    #velocityx.append(vx)
    #velocityy.append(vy)
print(t)
print(xpos,ypos)
plt.plot(xpos,ypos)
plt.title("Boat trajectory x-y")
plt.show()
    
    
    

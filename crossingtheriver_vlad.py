# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:21:37 2018

@author: Vlad Gavra
"""

import numpy as np
import matplotlib.pyplot as plt

def v_water(y):
    return A*np.sin(pi*y/L)

#constants
L=100. #m
A=12.  #m/s
v=10 #m/s -- boat speed (ct.)
pi=3.14159
phi=0  #control angle -- rad
dt=0.001 #s
x=0.  #origin at the starting point
y=0.
vx=10*np.sin(phi) #m/s  #relative to the ground
vy=10*np.cos(phi) #m/s
t=0
hor=np.array([])
ver=np.array([])
while y<=L:
    x+=vx*dt
    y+=vy*dt
    water=v_water(y)
    vx=v*np.cos(phi)+water
    vy=max(v*np.sin(phi),0.00001)
    
    phi=np.arctan(vx/vy) #plug in function for phi
    
    hor=np.append(hor,x)
    ver=np.append(ver,y)
    t+=dt

print(t)


plt.plot(hor,ver,'r--')
plt.title("Boat trajectory with respect to the ground")
plt.show()

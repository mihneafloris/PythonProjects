#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medieval catapult assignmetn
Floris Mihnea
4663675

"""

from math import pi, sqrt, radians, sin, cos
import assignment_catapult
import numpy as np
from matplotlib import pyplot as plt

print("Medieval Catapult Simulation")
print()
print("Please enter the following input variables: ")


R = float(input("Enter the arm length R[m]: "))
phi = float(input("Enter start angle phi [degrees]: "))
phistop= float(input('Enter the stop angle Phi [degrees]: '))
L_0= float(input('Enter the unstrechted spring length L_0 [m]: '))
k_elastic= float(input('Enter the spring constant k [N/m]: '))
m= float(input('Enter the mass of the stone [kg]: '))

phi= radians(phi)
phistop= radians(phistop)

g0= 9.81 #[m/s^2]
rhorock = 1600 #[kg/m^3]
rho_air = 1.225 #[kg/m^3]
C_D  = 0.7


speed1 = assignment_catapult.main(R,phi,phistop,L_0,k_elastic,m)[5]
print ("The launch speed is equal to: ", round (speed1[-1],3), "m/s")

xvals3 = assignment_catapult.main(R,phi,phistop,L_0,k_elastic,m)[0]
print("The distance reached is equal to: ", round(xvals3[-1],3), "m")



# Convert lists into numpy arrays
time3 = assignment_catapult.main(R,phi,phistop,L_0,k_elastic,m)[2]
yvals3 = assignment_catapult.main(R,phi,phistop,L_0,k_elastic,m)[1]
inclination3 = assignment_catapult.main(R,phi,phistop,L_0,k_elastic,m)[4]
speed3 = assignment_catapult.main(R,phi,phistop,L_0,k_elastic,m)[3]
t = np.asarray(time3)
x = np.asarray(xvals3)
y = np.asarray(yvals3)
incl = np.asarray(inclination3)
spd3 = np.asarray(speed3)

#Make plots

plt.suptitle("Trajectory plot")
plt.subplot(2,2,1)
plt.title("height vs distance")
plt.plot(x,y)
plt.xlabel("distance[m]")
plt.ylabel("height[m]")

plt.subplot(2,2,2)
plt.title("height vs time")
plt.plot(t,y)
plt.xlabel("time[s]")
plt.ylabel("height[m]")

plt.subplot(2,2,3)
plt.title("inclination vs time")
plt.plot(t,incl)
plt.xlabel("time[s]")
plt.ylabel("inclination[degrees]")

plt.subplot(2,2,4)
plt.title("speed vs time")
plt.plot(t,spd3)
plt.xlabel("time[s]")
plt.ylabel("speed[m/s]")







plt.subplots_adjust(left=None, bottom=0.1, right=None, top=None,
                wspace=0.3, hspace=0.5)
plt.show()

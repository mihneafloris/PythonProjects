import math
from math import *
import matplotlib.pyplot as plt


#input numbers/variables
phi = 0 #rad
phistop = pi/3 #rad
R= 3 #meters
L_0= 0.5 #meters
m= 90 #kg
k_elastic= 5000 #N/m
rho_rock= 1600 #kg/m^3
rho_air= 1.225 #kg/m^3
C_D=0.7 #dimensionless
V_sphere=(m/rho_rock) #m^3
r_rock= (V_sphere*3/4/pi)**(1/3)
S_sphere= pi* r_rock**2
c=0.5*rho_air*C_D*S_sphere
pi = math.pi
g_0=9.81 #m/s^2
dt=0.0001
def main(R=R,phi=phi,phistop=phistop,L_0=L_0,k_elastic=k_elastic,m=m):
    t=0
    v=0
    phi=0.0
    v_ang=0.0
    alpha=pi/4
    degrees=0
    xvals=[]
    yvals=[]
    speed1=[]
    inclination=[]
    time=[]
    speed2=[]
    while degrees<=phistop:
        L_elas= R* math.sin(pi/2-phi)/math.sin(alpha+phi)
        F_elas=k_elastic*(L_elas - L_0)
        F_grav=m*g_0
        F_tangent= F_elas * math.sin(alpha+phi)-F_grav*math.cos(phi)
        a= F_tangent/m
        a_ang=a/R
        v_ang=v_ang + a_ang*dt
        phi= phi + v_ang *dt
        alpha=(pi/2-phi)/2
        v = v_ang *R
        t= t +dt
        speed1.append(v)
        degrees=phi
        #print(degrees)
        #print(v)
    
    h= R * math.sin(math.radians(60))
    slope = math.tan(math.radians(30))
    angle = 30
    v_x= v* math.cos(math.radians(30))
    v_y = v * math.sin(math.radians(30))
    x=-R * math.cos(math.radians(60))
    while h>0:
        F_drag= c * v**2
        F_drag_x = F_drag * math.cos(math.radians(angle))
        F_drag_y = F_drag * math.sin(math.radians(angle))
        F_gravity=m*g_0
        a_x= F_drag_x/m
        a_y=(F_drag_y+F_gravity)/m
        v_x = v_x - a_x * dt
        v_y = v_y - a_y *dt
        angle = math.degrees(math.atan(v_y/v_x))
        x = x + v_x * dt
        h = h + v_y * dt
        t = t + dt
        #print(h)
        speed2.append(math.sqrt(v_y**2 + v_x**2))
        inclination.append(angle)
        time.append(t)
        xvals.append(x)
        yvals.append(h)

    return xvals, yvals,time,speed2,inclination,speed1
    speed1=[]
    inclination=[]
    time=[]
    speed2=[]
    while degrees<=phistop:
        L_elas= R* math.sin(pi/2-phi)/math.sin(alpha+phi)
        F_elas=k_elastic*(L_elas - L_0)
        F_grav=m*g_0
        F_tangent= F_elas * math.sin(alpha+phi)-F_grav*math.cos(phi)
        a= F_tangent/m
        a_ang=a/R
        v_ang=v_ang + a_ang*dt
        phi= phi + v_ang *dt
        alpha=(pi/2-phi)/2
        v = v_ang *R
        t= t +dt
        speed1.append(v)
        degrees=phi
        #print(degrees)
        #print(v)
    
    h= R * math.sin(math.radians(60))
    slope = math.tan(math.radians(30))
    angle = 30
    v_x= v* math.cos(math.radians(30))
    v_y = v * math.sin(math.radians(30))
    x=-R * math.cos(math.radians(60))
    while h>0:
        F_drag= c * v**2
        F_drag_x = F_drag * math.cos(math.radians(angle))
        F_drag_y = F_drag * math.sin(math.radians(angle))
        F_gravity=m*g_0
        a_x= F_drag_x/m
        a_y=(F_drag_y+F_gravity)/m
        v_x = v_x - a_x * dt
        v_y = v_y - a_y *dt
        angle = math.degrees(math.atan(v_y/v_x))
        x = x + v_x * dt
        h = h + v_y * dt
        t = t + dt
        #print(h)
        speed2.append(math.sqrt(v_y**2 + v_x**2))
        inclination.append(angle)
        time.append(t)
        xvals.append(x)
        yvals.append(h)

    return xvals, yvals,time,speed2,inclination,speed1

arg1, arg2, arg3, arg4, arg5, arg6=main()
print(arg1[-1])
print(arg6[-1])
plt.plot(arg1, arg2)
plt.show()
plt.plot(arg3, arg4)
plt.show()
plt.plot(arg3, arg5)
plt.show()









    

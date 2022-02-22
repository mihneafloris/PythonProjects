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
def main(R,phi,phistop,L_0,k_elastic,m):
    t=0
    v=0
    phi=0.0
    v_ang=0.0
    alpha=pi/4
    degrees=0
    xvals1=[]
    yvals1=[]
    speed1=[]
    time1=[]
    inclination1=[]
    
    speed2=[]
    xvals2=[]
    yvals2=[]
    time2=[]
    inclination2=[]

    speed3=[]
    xvals3=[]
    yvals3=[]
    inclination3=[]
    time3=[]
    while degrees<=phistop:
        L_elas= R* math.sin(pi/2-phi)/math.sin(alpha+phi)
        F_elas=k_elastic*(L_elas - L_0)
        F_grav=m*g_0
        F_tangent= F_elas * math.sin(alpha+phi)-F_grav*math.cos(phi)
        a= F_tangent/m
        a_ang=a/R
        v_ang=v_ang + a_ang*dt
        phi= phi + v_ang *dt
        
        v = v_ang *R
        t= t +dt
        x= - R* math.cos(phi)
        y= R*math.sin(phi)
        V_x_1=v*cos(alpha)
        V_y_1=v*sin(alpha)
        alpha=(pi/2-phi)/2
        launchangle = atan(V_y_1/V_x_1)
        inclination1.append(launchangle)
        speed1.append(v)
        xvals1.append(x)
        yvals1.append(y)
        time1.append(t)
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
        inclination2.append(angle)
        time2.append(t)
        xvals2.append(x)
        yvals2.append(h)

    xvals3.extend(xvals1 + xvals2)
    yvals3.extend(yvals1 + yvals2)
    speed3.extend(speed1 + speed2)
    time3.extend(time1 + time2)
    inclination3.extend(inclination1 +inclination2)
    return xvals3, yvals3,time3,speed3,inclination3,speed1













    

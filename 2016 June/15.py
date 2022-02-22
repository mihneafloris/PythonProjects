import math 

C_L = 1.45
C_D0=0.035
dragpolar=23.8761 #pi*A*E
rho= 1.2225
S =102
g=9.80665
m=41467 #kg
V_takeoff= 67
T= 180000 #2x 90kN
miu = 0.03 #friction coefficient

#wheel frictino drag force will be 3% of the normal force on the wheels at start

#normal force decreases over time because of lift

dt=0.001

#should reach 30 m/a after 7.48 seconds

#time before aircraft takes off? (4 significant digits)
#required runway length? (3 significant digits)
v=0
s=0
t=0
while v<V_takeoff:
    D_aero = (C_D0 + (C_L**2)/23.8761) *0.5 * rho *v*v*S
    L = C_L*0.5*1.225*v*v*S
    N=m*g-L
    D_friction = N *miu
    D_total = D_aero+D_friction
    force=T-D_total
    a=force/m
    v=v+a*dt
    s=s+v*dt
    t=t+dt

print(t,s)

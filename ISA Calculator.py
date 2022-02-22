#Floris Mihnea
#Student number: 4663675
#Assignment 1
from math import *
print("Troposphere calculator")

print ( "1. Calculate ISA for altitude in meter")
print ( "2. Calculate ISA for altitude in feet")
print ( "3. Calculate ISA for altitude in FL")

choice = int(input("Enter your choice;"))

if choice is 1:
    h = float(input("Enter altitutude[m]:"))
elif choice is 2:
    ft = 0.3048
    h_feet = float (input("Enter altitude [feet]:"))
    h = ft* h_feet
elif choice is 3:
    ft = 0.3048
    h_FL= float(input("Enter altitude [FL]:"))
    h = h_FL *100 * ft
else:
    raise ValueError ("Wrong chioce!")
    
    
p_sea = 101325.0 #[Pa]
R_air = 287.058 #[J/(kg*K)]
g_0 = 9.80665 #[m/s^2]
T_sea = 288.15 #[K]
rho_sea = p_sea/(R_air*T_sea) #[kg/m^3]


#ISA Calculator

if h > 0:
    name = "troposphere"
    h_1 = min(h, 11000)
    h_0 = 0
    a = -0.0065
    
    T_1 = T_sea + a*(h_1-h_0)
    p_1 = p_sea*(T_1/T_sea)**(-g_0/(a*R_air))
    rho_1 = p_1/(R_air*T_1)

elif h > 11000:
    name = "tropopause"
    h_1 = min(h, 20000)
    h_0 = 11000
    a = 0.0
    T_0 = T_1
    p_0 = p_1

    T_1 = T_0 + a*(h_1-h_0)
    p_1 = p_0*exp(-g_0/(R_air*T_1)*(h_1-h_0))
    rho_1 = p_1/(R_air*T_1)

elif h > 20000:
    name: "stratosphere"
    h_1 = min(h, 32000)
    h_0 = 20000
    a = 0.0010
    T_0 = T_1
    p_0 = p_1
    T_1 = T_0 + a*(h_1-h_0)
    p_1 = p_0*(T_1/T_0)**(-g_0/(a*R_air))
    rho_1 = p_1/(R_air*T_1)

elif h > 32000:
    name = "stratosphere"
    h_1 = min(h, 47000)
    h_0 = 32000
    a = 0.0028
    T_0 = T_1
    p_0 = p_1
    T_1 = T_0 + a*(h_1-h_0)
    p_1 = p_0*(T_1/T_0)**(-g_0/(a*R_air))
    rho_1 = p_1/(R_air*T_1)

elif h > 47000:
    name = "statopause"
    h_1 = min(h, 51000)
    h_0 = 47000
    a = 0.0
    T_0 = T_1
    p_0 = p_1
    T_1 = T_0 + a*(h_1-h_0)
    p_1 = p_0*exp(-g_0/(R_air*T_1)*(h_1-h_0))
    rho_1 = p_1/(R_air*T_1)

elif h > 51000:
    name = "mesosphere"
    h_1 = min(h, 71000)
    h_0 = 51000
    a = -0.0028
    T_0 = T_1
    p_0 = p_1
    T_1 = T_0 + a*(h_1-h_0)
    p_1 = p_0*(T_1/T_0)**(-g_0/(a*R_air))
    rho_1 = p_1/(R_air*T_1)

elif 71000 < h < 86000:
    name = "mesosphere"
    h_1 = min(h, 86000)
    h_0 = 71000
    a = -0.0020
    T_0 = T_1
    p_0 = p_1
    T_1 = T_0 + a*(h_1-h_0)
    p_1 = p_0*(T_1/T_0)**(-g_0/(a*R_air))
    rho_1 = p_1/(R_air*T_1)

print("Ready")

print ( "Temperature: [K]", round( T_1,4))
print ( "Presure:  [Pa]", round(p_1,4))
print ( "Density: [kg/m^3]", round(rho_1,8))

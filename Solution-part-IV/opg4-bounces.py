from math import *
from matplotlib.pyplot import *

# Init pos and angle
x   = 0.0 #[m]
y   = 0.0 #[m]
phi = 0.8  #[rad]

# Plot tables
xtab = []
ytab = []
phitab = []
xtab.append(x)
ytab.append(y)


# bounce counter
nbounce = 0

# until leaving box


while x >= 0.0:

# Update position    
    x = x + 0.001*cos(phi)
    y = y + 0.001*sin(phi)

# Check for edges:

# Vertical edges:
    if x>1.8:
        x = 1.8-(x-1.8)
        phi = pi - phi
        nbounce = nbounce+1
        print("Xmax Bounce",nbounce)
    elif x<0.0:
        if abs(y)>0.2 or nbounce==41:
            x = -x
            phi = pi - phi
            nbounce = nbounce+1
            print("Xmin Bounce",nbounce)
        else:
            print("Yes, I'm free!")
            print()

# Horizontal edges:
    if y>2.0:
        phi = (-phi)%(2.*pi)
        y = 2.0-(y-2.0)
        nbounce = nbounce+1
        print("Ymax Bounce",nbounce)

    elif y<-1.0:
        phi = (2.*pi-phi)
        y = -1.+(-1.-y)
        nbounce = nbounce+1
        print("Ymin Bounce",nbounce)

    xtab.append(x)
    ytab.append(y)
    phitab.append(phi)

# plot Trajectory
plot(xtab,ytab)

# draw box
xbox = [0.0,0.0,1.8,1.8,0.0,0.0]
ybox = [0.2,2.0,2.0,-1.0,-1.0,-0.2]
plot(xbox,ybox,'r-')


show()

print (nbounce," bounces in total!")

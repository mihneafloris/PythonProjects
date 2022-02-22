from math import *

import matplotlib as mplt
import matplotlib.pyplot as plt
phi = 0.8


x0 = 0.001
y0 = 0.001

xboundmin = 0.
xboundmax = 1.8
yboundmin = -1.
yboundmax = 2.

xtab = []
ytab = []

directionx = 1
directiony = 1
bouncex = 0
bouncey = 0
bounce = 0

running = True

while running:
    x = x0 + directionx*0.001*cos(phi)
    y = y0 + directiony*0.001*sin(phi)

    xtab.append(x)
    ytab.append(y)

    x0 = x
    y0 = y

    if x <= 0. and (y >= -0.2 and y <= 0.2):
        running = False
        bounced = False


    bounced = False
    if x > xboundmax:
        directionx *= -1
        bounced = True
        print("xmax bouncex %s" % bouncex)
        x = xboundmax - (x-xboundmax)

    elif x < xboundmin:
        directionx *= -1
        bounced = True
        print("xmin bouncex %s" % bouncex)
        x = xboundmin + (xboundmin-x)

    if y > yboundmax:
        y = yboundmax - (y-yboundmax)
        directiony *= -1
        bounced = True
        print("ymax bouncex %s" % bouncex)

    elif y < yboundmin:
        y = yboundmin + (yboundmin-y)
        directiony *= -1
        bounced = True
        print("ymin bouncex %s" % bouncex)

    if bounced and running:
        bounce+=1


plt.plot(xtab,ytab)
print(bounce)

plt.show()

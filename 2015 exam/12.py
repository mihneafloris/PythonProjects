import matplotlib.pyplot as plt
from math import *
import numpy as np

x=np.linspace(-7,7,14000,endpoint=True)
ytab=[]
gtab=[]
for i in x:
    y= np.sin(i) * (0.003*i**4 - 0.1 * i**3 +i**2 +4*i+3)
    ytab.append(y)
    g = -10* np.arctan(i)
    gtab.append(g)
plt.plot(x,ytab,'r')
plt.plot(x,gtab,'b')
plt.show()
                 
    

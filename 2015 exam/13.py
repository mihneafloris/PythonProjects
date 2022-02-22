from math import *
import numpy as np
s=0
for i in range(1,5001):
    y=1/i**2 *np.cos(i*pi*0.4)
    s=s+y

print(s)

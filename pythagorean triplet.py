#pytgagorean triplet numpy way(first way was nested for loops)

import numpy as np
from numpy import *


N=1000
A= ones((N-2,N-2))
a=array([list(range(1,N-1))])*A
b=array([list(range(1,N-1))]).T*A

c= (sqrt(a*a+b*b).astype(int)
sw = (a*a+b*b==c*c)*(a+b+c==1000) 
print(a[sw],b[sw],c[sw])

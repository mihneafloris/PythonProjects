import numpy as np
from matplotlib import pyplot as plt
a = np.zeros((4,4))
#x=np.arange(0.,10.01,0.01)
x =np.linspace(0.,10.,1000)
y=np.sin(x)
y1=x*x-2*x-1

plt.plot(x,y)
plt.plot(x,y1)
plt.show()

from math import *

M = 5000
x = 0.4

total = 0.0

for i in range(1,M):
    n = float(i)
    
    total = total + (1./(n*n))*cos(n*pi*x)

print(total)

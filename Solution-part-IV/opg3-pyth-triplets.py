from math import *

# Pythagorean triplets

#for N  in range(20,21):
#for N  in range(100,101):
#for N in range(100,1000,10):
for N in range(810,820):
 
    n = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            c2 = i*i+j*j
            c = int(sqrt(c2))
            if c*c==c2:
                n = n+1
    #            print n,(i,j,c)
                
    print(n," triplets found for N =",N)

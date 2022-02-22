import math as m
import numpy as np
listofbestnumbers=[]
maximum=0
for ognumber in range(2,30000):
    i=ognumber
    k=0
    while i!=1:
       
        if i%2==0:
            i=i/2
            k=k+1
        else:
            i=i*3+1
            k=0
    if k>maximum:
        listofbestnumbers=[ognumber]
        maximum=k
    elif k == maximum:
        listofbestnumbers.append(ognumber)
        
print(listofbestnumbers, maximum)

        

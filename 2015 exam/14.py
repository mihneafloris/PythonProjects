import numpy as np
from math import *

lst=[]
for n in range(0,1001):
    isjuf= False
    if n%7==0:
        isjuf= True
    if n%11==0:
        isjuf =True
    string=str(n)
    for i in range(len(string)):
        if string[i]=="7":
            isjuf=True
    for i in range(len(string)-1):
        if string[i]=="1" and string[i+1]=="1":
            isjuf=True
    if isjuf==False:
        lst.append(n)

print(sum(lst))



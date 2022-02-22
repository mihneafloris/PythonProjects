# -*- coding: utf-8 -*-
import math
from math import *
import numpy as np
#constructing a list of primes up to 100
listofprimes=[]

for num in range(1,1000):
    if num>1:
        #check for factors
        for i in range(2,num):
            if (num%i)!= 0:
                listofprimes.append(num)
            else:
                break
                
print(listofprimes)
#constructing 

import math as m
s=0 
for n in range(1,100000000):
    sequence= (-1)* (2*n+1)/(3*n+2)
    s1=s
    s=s+ sequence
    if s1-0.0000001<s<s1+0.0000001:
        break

print(s)

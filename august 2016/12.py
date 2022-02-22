import math as m
numbers=[]
for number in range(1,10001):
    x=str(number)
    s=0
    for k in range(0,len(x)):
        b=int(x[k])
        c=m.factorial(b)
        s=s+c
    if s%number==0:
        numbers.append(number)

print(numbers[-1],numbers[-2])
    

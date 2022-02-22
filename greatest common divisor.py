import math as m

a=int(input("Insert first number: "))
b=int(input("Insert second number: "))
r=1
while r!=0:
    if b>a:
        r=b%a
        b=r
    else:
        r=a%b
        a=r

print(a,b)
    

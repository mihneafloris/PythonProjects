import math as m

def l2m(x):
    k=0
    while x>99:
        x=str(x)
        lastdigit=int(x[-1])
        x=x[:-1]
        x=int(x)-2*lastdigit
        k=k+1
    print(k,x)

print(l2m(345678))

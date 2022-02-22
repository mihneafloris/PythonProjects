import math as m

def L2M(x):
    k=0
    while x>99:
        stringx=str(x)
        lastdigit = int(stringx[-1])
        stringx = stringx[:-1]
        x= int(stringx) - 2*lastdigit
        k=k+1
    print(k,x)
    
print(L2M(345678))

#87425473459527629989378641469

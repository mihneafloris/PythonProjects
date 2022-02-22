import math as m
xpos=[]
ypos=[]
n= input("Input number of points: ")
for i in range(int(n)):
    x=input("enter x position:")
    xpos.append(x)
    i=i+1

for i in range(int(n)):
    y=input("enter y position:")
    ypos.append(y)
    i=i+1          

A=0
xpos = [int(i) for i in xpos]
ypos = [int(i) for i in ypos]
for i in range(len(xpos)-1):
    A= (ypos[i+1]+ypos[i])/(xpos[i+1]-xpos[i])/2

print(A)

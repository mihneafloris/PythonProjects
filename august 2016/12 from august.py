import math as m
divisiblenumbers=[]

for number in range(1,10000):
    sumoffactorials=0
    strofnumber=str(number)
    for digit in strofnumber:
        sumoffactorials=sumoffactorials+m.factorial(int(digit))
    if sumoffactorials%number==0:
        divisiblenumbers.append(number)

print(divisiblenumbers[-1],divisiblenumbers[-2])

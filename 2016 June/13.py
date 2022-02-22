listofnumbers =[]
n=0
while n<1000:
    counter = 0
    temp = n
    for i in range(10,-1,-1):
        if not 2**i>temp:
            temp=temp%(2**i)
            counter=counter+1
    if counter%2==0 and counter!=0:
        listofnumbers.append(n)
    n=n+1
print(listofnumbers)
print(sum(listofnumbers))
    

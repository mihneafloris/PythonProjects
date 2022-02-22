import math 
n= input("Inser n: ")
k= input("Inser k: ")
combinations = math.factorial(int(n))/math.factorial(int(k))/math.factorial(int(n)-int(k))
print("Combinations of n over k is: ", combinations) 

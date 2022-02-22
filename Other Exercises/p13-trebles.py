import math
from math import *
from collections import Counter

N = 100000
numbers = []
for k in range (10000,N):
    number_string = str(k)
    k = k *3
    number_string_multiplied = str (k)
    if Counter(number_string) == Counter(number_string_multiplied):
        numbers.append(number_string)

print(numbers,sep=", ")
numbers1=[int(i) for i in numbers]

sum_final = sum(numbers1)
print(sum_final)
    

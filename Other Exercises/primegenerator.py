from numpy import *

N = 32000

primes = array(range(0,N)) # each value is equal to the index of the value


#0, 1 are not prime numbers

primes[0:2]= -1 #negative means no prime

for k in range(2,N):
    if primes[k]>0: # is a prime
        primes[2*k:N:k] = -1 # sieve function
        
#show result
print(list(primes[primes>0]))

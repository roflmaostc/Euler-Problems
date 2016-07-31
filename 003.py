#!/usr/bin/env python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np

def findPrimes(number):
    limit=int(np.sqrt(number)//1)
    #create odd numbers up to sqrt(number)
    numbers=[i+1 for i in range(1,limit)]
    #add 2 
    numbers=[2]+numbers
    #only odd numbers
    numbers=numbers[::2]
    #list for the prime factors
    primes=[]
    
    i=0
    
    while number>2:
        #check if prie
        while number%numbers[i]==0 and i-1<limit:
                primes.append(numbers[i])
                number=number/numbers[i]
                
        i+=1
    return primes

print(findPrimes(600851475143))



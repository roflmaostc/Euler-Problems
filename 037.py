#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def isPrime(number):
    import numpy as np
    if number==1:
        return False
    if number==2:
        return True
    if number%2==0:
        return False
    for i in range(3, int(np.sqrt(number)//1)+1,2 ):
        if number%i==0:
            return False
    return True

def findPrimes(limit):
    primes=[2]
    for i in range(3,int(limit)):
        if isPrime(i)==True:
            primes.append(i)        
    return primes 

def leftRemoving(number):
    number=str(number)
    for i in range(1, len(number)):
        if isPrime(int(number[0:i]))!=True:
            return False
    return True

def rightRemoving(number):
    number=str(number)
    for i in range(1, len(number)):
        if isPrime(int(number[i:]))!=True:
            return False
    return True

def solveProblem():
    primes=findPrimes(1e6)
    truncutablaPrimes=[]
    for prime in primes:    
        if rightRemoving(prime)==True and leftRemoving(prime)==True and prime>7:
            truncutablaPrimes.append(prime)
    return truncutablaPrimes 

def sumUpAll(liste):
    return sum(a for a in liste)

print(sumUpAll(solveProblem()))

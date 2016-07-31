#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np

def isPrime(number):
    for i in range(2, int(np.sqrt(number)//1)+1):
        if number%i==0:
            return False
    return True

def findPrimes(limit):
    sum=2
    prime=2
    for i in range(3,limit):
        if isPrime(i)==True:
            sum+=i
    return sum

print(findPrimes(int(2e6)))

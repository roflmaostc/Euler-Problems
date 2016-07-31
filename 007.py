#!/usr/bin/env python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import numpy as np

def isPrime(number):
    for i in range(2, int(np.sqrt(number)//1)+1):
        if number%i==0:
            return False
    return True


def findNthPrime(n):
    counter=1
    prime=2
    for i in range(3,int(1e7),2):
        if isPrime(i)==True:
            counter+=1
            prime=i
            if counter ==n:
                return prime

print(findNthPrime(10001))

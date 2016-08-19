#!/usr/bin/env python

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def solveProblem(limit=1e6):
    specialPrimes=[]

    for number in range(2,int(limit)):
        if allCycles(str(number))==True:
            specialPrimes.append(int(number))

    print(specialPrimes)
    return len(specialPrimes)
def allCycles(number):
    """Number must be a string to prevent the removing of the leading zero. 
       101 -> 11 -> 11 is wrong
       101 -> 011 -> 110 is rigth"""
    cycled=0
    while cycled<len(str(number)):
        if isPrime(int(number))==False:
            return False
        number=cycleNumber(number)
        cycled+=1
    return True



def cycleNumber(number):
    return str(number)[-1]+str(number)[0:-1]


def isPrime(number):
    """Simple and dumb  method to check if a number is prime"""
    from math import sqrt
    if number<2:
        return False
    elif number==2:
        return True
    elif number%2==0:
        return False
    for i in range(3,int(sqrt(number)//1)+1,2):
        if number%i==0:
            return False
    return True


print(solveProblem())

#!/usr/bin/env python

"""
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""



def isPrime(number):
    """Simple method to check if a number is prime"""
    from math import sqrt
    if number<2:
        return False
    if number%2==0:
        return False
    for i in range(3,int(sqrt(number)//1)+1,2):
        if number%i==0:
            return False
    return True



def iterateFunction(a,b):
    """Iterates over the function and counts how many consecutive primes it procudes"""
    f = lambda x: x**2+a*x+b

    counter = 0
    while True:
        if isPrime(f(counter))==False:
            return counter
        else:
            counter+=1

    return counter

def solveProblem(aLimit=1000, bLimit=1000):
    nMax=0
    aBest=0
    bBest=0
    for a in range(-aLimit+1,aLimit):
        for b in range(-bLimit,bLimit+1):
            cons=iterateFunction(a,b)
            if cons>nMax:
                nMax=cons
                aBest=a
                bBest=b

    return aBest*bBest,  nMax

print(solveProblem())

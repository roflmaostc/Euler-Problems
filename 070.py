#!/usr/bin/python

"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""


from eulerfunctions import  phi, generate_primes, isPrime
from math import log10

def is_permutation(a, b):
    if int(log10(a)) != int(log10(b)): 
        return False
    
    a = list(str(a))
    b = list(str(b))
    a.sort()
    b.sort()
    return a==b


def phi_hm(n, primes, hm):
    if n in hm:
        return hm[n]
       
    res = phi(n, primes)
    if res%2 == 1:
        hm[2*n] = res
        return res
    if res%3 != 0:
        hm[3*n] = 2*res
    if res%5 != 0:
        hm[5*n] = 4*res
    if res%7 != 0:
        hm[7*n] = 6*res

    return res


def main():
    primes = generate_primes(round(10**3.5))

    hm = dict()
    min = 1000000
    minn = 0
    for i in range(2,10**7):
        res = phi_hm(i, primes, hm)
        if is_permutation(i, res):
            if i/res < min:
                min = i/res
                minn = i
    return minn
print(main())

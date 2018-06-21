#!/usr/bin/python

"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""


from eulerfunctions import gcd

def main():
    target = 3/7
    best = 1
    
    n = 428572
    bestn = n 
    bestd = 1 
    d = 1000000
    while d>8:

        if n/d >= target:
            n -= 1
        else:
            d -= 1

        if n/d > target:
            continue

        if abs((n/d-target))<best and gcd(n,d) == 1:
            bestn = n
            bestd = d
            best = abs(n/d-target)
    return bestn

print(main())

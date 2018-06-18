#!/usr/bin/python

"""
Problem 064
"""

from math import floor, sqrt
from eulerfunctions import is_square

def generate_a(n):
    d = dict() 
    a = []
    a0 = floor(sqrt(n))
    a.append(a0)
    S = n
    diff = a0
    N = n-a0**2
    Z = 1
    i = 1

    #representation of fraction as: (Z*(sqrt(S)+diff)/N)
    #third binomial formula
    while True:
        N = N/Z
        Z = 1
        ai = floor( (sqrt(S)+diff)/N)
        diff -= ai*N
        a.append(ai)
        Z = N
        N = S-diff**2
        diff = abs(diff)
        if (Z,N,diff) in d:
            return i-1
        else:
            d[(Z,N,diff)] = i

        i += 1
    
    return 
def main():
    N = 10000
    
    x = 0
    for i in range(2,N+1):
        if is_square(i):
            continue
        
        r = generate_a(i)
        if r % 2 == 1:
            x += 1
    
    return x

print(main())

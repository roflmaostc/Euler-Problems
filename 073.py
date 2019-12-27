#!/usr/bin/python
"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

# would be also possible to implement via prime factors comparison
from fractions import Fraction
from math import floor, ceil

def main(max_d=12000):
    visited = dict()
    for d in range(1, max_d + 1):
        for n in range(floor(1/3 * d), ceil(1/2 * d) + 1):
            frac = Fraction(n, d)
            num = frac.numerator
            den = frac.denominator
            if 1 / 3  < num / den < 1 / 2:
                visited[(num, den)] = True
    
    return len(visited)

print(main())

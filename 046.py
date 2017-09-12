#!/usr/bin/env python


"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from eulerfunctions import isPrime
from math import floor,sqrt


def solveProblem():
    
    for i in range(9, 10000,2):
        if isPrime(i):
            True
        else:
            worked = False
            j = 1
            res = i-2*j**2
            while res > 2:
                if isPrime(res):
                    worked = True
                j += 1
                res = i-2*j**2
            if worked == False:
                return i
    return 1


print(solveProblem())

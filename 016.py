#!/usr/bin/env python

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def solveProblem(power=1000, base=2):
    return int(sum(int(i) for i in str(2**1000)))

print(solveProblem())

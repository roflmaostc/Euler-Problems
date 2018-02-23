#!/usr/bin/env python


"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""


from eulerfunctions import crossfoot as cf

def solve(n):
    max = 0
    for a in range(100):
        for b in range(100):
            t = cf(a**b)
            if t>max:
                max = t
    return max 

print(solve(100))

#!/usr/bin/env python

"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x,
4x, 5x, and 6x, contain the same digits.
"""

def solve_problem():
    """solves problem"""
    num = 0
    while True:
        num += 1
        for fac in range(2, 7):
            if set(str(num)) != set(str(num*fac)):
                break
            if fac == 6:
                return num

print(solve_problem())

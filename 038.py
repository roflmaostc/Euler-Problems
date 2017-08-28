#!/usr/bin/env python

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import math

def concatenate(base, number):
    return base*10**(1+math.floor(math.log10(number)))+number

def checkIfValid(number):
    s = str(number)

    for i in range(1,10):
        if str(i) not in s:
            return False

    return True


def solveProblem():
    max = 0

    for i in range(1,10**5):
        base = i
        j = 2
        while base<10**9:
            max = base if base > max and checkIfValid(base) else max  
            base = concatenate(base, i*j)
            j += 1

    return max

print(solveProblem())

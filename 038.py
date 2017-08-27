#!/usr/bin/env python

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

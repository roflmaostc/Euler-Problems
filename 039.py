#!/usr/bin/env python

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

"""
My idea is to iterate over a and b, and calculate c with sqrt(a^2+b^2). Then check if c is integer and a+b+c<=p. Then increment the pCounter Array at right position
"""

import numpy as np

def validTriangle(a,b,p):
    c = np.sqrt(a**2+b**2)
    if  c % 1 !=0 :
        return False
    if a+b+c>p:
        return False

    return True


def solveProblem():
    p = 1000
    pCounter = np.zeros(1001)

    for a in range(1,p):
        for b in range(1,p):
            if validTriangle(a,b,p):
                c = int(np.sqrt(a**2+b**2))
                pCounter[a+b+c] +=1

    return np.argmax(pCounter)

print(solveProblem())

#!/usr/bin/env python
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial as fac

def simpleMath(gridSize=20):
    return int(fac(40)/fac(20)/fac(20))


print(simpleMath())

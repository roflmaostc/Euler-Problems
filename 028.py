#!/usr/bin/env python

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import tabulate

def createSpiral(size):
    """Creates spiral with numbers. Requires odd size"""
    grid=[[0 for i in range(size)] for i in range(size) ]
    if size%2==0:
        return []
    else:
        i,j=size//2,size//2
        for value in range(1,size**2+1):
            grid[i][j]=value
            i,j=giveNewField(i,j,size)
    return grid

def giveNewField(i, j, size):
    """Returns the next field for the spiral"""
    if j>=i and i+j<size:
        return i,j+1
    elif i<j:
        return i+1,j
    elif j<=i and i+j>=size:
        return i,j-1
    else:
        return i-1,j


def sumDiagonals(grid):
    diag1=sum(grid[i][i] for i in range(len(grid)))
    diag2=sum(grid[len(grid)-i-1][i] for i in range(len(grid)))
    return diag1+diag2-1


def sumDiagonalsSmart(size):
    """size>=3"""
    import numpy as np
    prev=np.array([3,5,7,9]) 
    diag=np.array([0,0,0,0])
    
    diag+=prev
    for i in range(1, size//2):
        prev=prev+[2,4,6,8]+8*i 
        diag+=prev
    
    return sum(diag)+1

print(sumDiagonalsSmart(1001))
# print(sumDiagonals(createSpiral(1001)))

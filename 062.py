#!/usr/bin/env python


"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def number_to_key(n):
    n = str(n)
    l = [i for i in n]
    l.sort()
    s = ''.join(l)
    return s


#idea is to store digits and check if 5 times a specific digits set occurred 
def solveProblem():
    hm = dict()
    
    i = 1
    while True:
        k = number_to_key(i**3)
        if k not in hm:
            hm[k] = [i**3]
        else:
            hm[k] = hm[k]+[i**3]
       
        if len(hm[k]) == 5:
            return min(hm[k])
        
        i += 1

    return 0

print(solveProblem())

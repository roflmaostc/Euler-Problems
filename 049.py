#!/usr/bin/env python

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from eulerfunctions import generate_primes 


def solveProblem():
    plist = generate_primes(10000)

    plist = [i for i in plist if i>999]
    
    for p in plist:
        if not contains_digits(p, list(str(1487))):
            counter = 1
            for q in plist:
                if q != p and contains_digits(q, list(str(p))) and abs(q-p) % 3330==0:
                    for k in plist:
                        if k != p and k != q and contains_digits(k,list(str(p))) and abs(k-p) % 3330 ==0:
                            return int(str(p)+str(q)+str(k)) 
    

def contains_digits(n, digits):
    """Check if a number contains all digits of digits list"""
    s = str(n)
    for d in digits:
        if d not in s:
            return False
    for l in s:
        if l not in digits:
            return False
    return True


print(solveProblem())

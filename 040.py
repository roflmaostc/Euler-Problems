#!/usr/bin/env python

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""



def solveProblem():
    s = ""
    i = 1
    while len(s)<10**6:
        s += str(i)
        i += 1
    
    res = 1
    for i in range(1,7):
        res *= int(s[10**i-1])

    return res

print(solveProblem())

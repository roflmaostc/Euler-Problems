#!/usr/bin/env python3

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
  a^2 + b^2 = c^2

  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
  Find the product abc.
"""

def searchTriplet(number=1000):
    c=1000
    a=0
    b=0


def searchTriplet2(number=1000):
    for a in range(1,number//2-1):
        for b in range(1,number//2-1):
            if a**2+b**2==(number-a-b)**2:
                return a*b*(number-a-b)


def condition(a,b,c,number=1000):
    return a+b+c==number


print(searchTriplet2())

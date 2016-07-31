#!/usr/bin/env python3
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def find35(limit):
    sum=0
    for i in range(1, int(limit)):
        #check mod 3
        if i % 3 == 0:
            sum+=i
        #check mod 5
        if i % 5 == 0:
            sum+=i
            #remove double counted
            if i % 3 == 0:
                sum-=i
    return sum

print(find35(1E3))

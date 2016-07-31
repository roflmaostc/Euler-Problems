#!/usr/bin/env python3

"""


The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def squareSum(limit):
    summe=sum([i for i in range(1, limit+1)])
    summe=summe**2
    return summe

def sumOfSquares(limit):
    summe=sum([i**2 for i in range(1, limit+1)])
    return summe

print(squareSum(100)-sumOfSquares(100))

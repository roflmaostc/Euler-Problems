#!/usr/bin/env python

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def solveProblem(limit=3e5):
    number=3
    allCuriousNumbers=[]
    while number<limit:
        if checkIfCurious(number):
            allCuriousNumbers.append(number)
        number+=1
        
    return sum(allCuriousNumbers) 


def checkIfCurious(number):
    numberStr=str(number)
    
    sumNumbers=0
    for digit in numberStr:
        sumNumbers+=factorial(int(digit))

    if sumNumbers==number:
        return True
    
    return False

def factorial(number):
    product=1
    while number>1:
        product*=number
        number-=1
    return product


print(solveProblem())


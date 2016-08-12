#!/usr/bin/env python

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import numpy as np

def solveProblem():
    abundantNumbers=np.asarray(createAbundantNumbers(28123))
    sum=0
    for i in range(1,28123+1):
        if sumOfTwoAbundants(abundantNumbers,i)==False:
            sum+=i
    
    return sum

def sumOfTwoAbundants(abundantNumbers, number):
    i=0
    j=len(abundantNumbers)-1
    while i<=j:
        result=abundantNumbers[i]+abundantNumbers[j]
        if result<number:
            i+=1
        elif result>number:
            j-=1
        else:
            return True
    return False


def divisors(number):
    """Returns the divisors of a number as a list"""
    numberFix=number
    divisors=[1]
    i=2
    while number > i:
        if numberFix%i == 0:
            divisors.append(i)
            if numberFix//i!=i:
                divisors.append(numberFix//i)
            number = numberFix//i
        i+=1
    divisors.sort()
    return divisors

def checkIfMultiple(number, abundantNumbers):
    for i in range(len(abundantNumbers)):
        if i%abundantNumbers[i]==0:
            return True

def createAbundantNumbers(limit):
    abundant=[]
    for i in range(12,limit+1):
        divisorsList=divisors(i)
        if i%6==0:
            abundant.append(i)
        # elif checkIfMultiple(i,abundant):
        #     abundant.append(i)
        elif sum(divisorsList)>i:
            abundant.append(i)
        
    return abundant

# import time
# start=time.time()
print(solveProblem())
# print("end %f" %(time.time()-start))

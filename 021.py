#!/usr/bin/env python

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisorsDumb(number):
    """Dumb way for all divisors"""
    divisors=[]
    for i in range(1,number//2+1):
        if number%i==0:
            divisors.append(i)
    return divisors

def divisors(number):
    numberFix=number
    divisors=[1]
    i=2
    while number > i:
        if numberFix%i == 0:
            divisors.append(i)
            divisors.append(numberFix//i)
            number = numberFix//i
        i+=1

    divisors.sort()
    return divisors


def amicablePairs(limit):
    amicablePairs=[]  
    for i in range(1,limit):
        sumOfDivisors=sum(divisors(i))
        sumOfDivisors2=sum(divisors(sumOfDivisors))
        
        if i==sumOfDivisors2 and i!=sumOfDivisors and (sumOfDivisors,i) not in amicablePairs:
            amicablePairs.append((i,sumOfDivisors))    
    
    return amicablePairs

def sumAllAmicableNumbers(amicablePairs):
    return sum([i[0]+i[1] for i in amicablePairs])

print(sumAllAmicableNumbers(amicablePairs(10000))) 

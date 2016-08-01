#!/usr/bin/env python
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
     10: 1,2,5,10
     15: 1,3,5,15
     21: 1,3,7,21
     28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def triangleNumberRecursive(order):
    """Create triangle number recursive"""
    if order == 1:
        return 1
    return order+triangleNumber(order-1)

def triangleNumber(order):
    """Create triangle numbers linearly"""
    return order*(order+1)//2


def numberOfDivider(number):
    """Returns back the number of dividers. Only applicable for number \in {1,\infty}"""
    amount=2
    for i  in range(2,number//2+1):
        if number%i == 0:
            amount+=1
    return amount, number


def numberOfDivider2(number):
    amount=0
    limit=number
    i=1
    while i<limit:
        if number % i == 0:
            limit = number // i
            amount+=1
            if limit != i:
                amount+=1

        i+=1
    return amount,number

def solveProblem():
    for i in range(1,100000):
        amount, number=numberOfDivider2(triangleNumber(i))
        print("teiler:" +str(amount)+" number:" +str(number)) 
        if amount > 500:
            return number
    
    return 0

print(solveProblem())

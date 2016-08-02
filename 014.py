#!/usr/bin/env python

"""


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def solveProblem(border=int(1e6)):
        #stores for a specific number the amount of steps to reach 1
    seen={}
    max=0
    bestNumber=1
    for i in range(1, border):
        number=i
        counter=0
            #sequence until 1
        while number>1:
            number=manipulate(number)
            counter+=1
                #check if a number is already processed
            if number in seen.keys():
                counter+=seen[number]
                number=1
            #update maximum   
        if counter>max:
            max=counter
            bestNumber=i
        
        seen[i]=counter
    return bestNumber

def manipulate(n):
    if n%2==0:
        return manipulateEven(n)
    else:
        return manipulateOdd(n)

def manipulateEven(n):
    return n/2


def manipulateOdd(n):
    return 3*n+1



print(solveProblem())

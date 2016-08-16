#!/usr/bin/env python


"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2=0.5
    1/3=    0.(3)
    1/4=    0.25
    1/5=    0.2
    1/6=    0.1(6)
    1/7=    0.(142857)
    1/8=    0.125
    1/9=    0.(1)
    1/10=   0.1 

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


import numpy as np

def findReoccuring(number, precision=10000, patternLength=1000):
    """This methods finds reoccuring patterns in sequences""" 
        #iterate over the differnet startIndex
    for startIndex in range(0, precision//3):
            #iterate over the length 
        for length in range(1, patternLength):
                #this is the pattern 
            pattern=number[startIndex:startIndex+length]
                #variable if pattern failed
            error=False
            iterationIndex=startIndex
                #iterate over all digits and search for an error in the pattern
            while error==False and iterationIndex+length<precision-1:
                if not np.array_equal(pattern, number[iterationIndex:iterationIndex+length]):
                    error=True
                else: 
                    iterationIndex+=length
                #no error found -> pattern found
            if error==False:
                return length

        #no pattern found in the given range
    return -1

    
    
def division(number, divisor, precision=10000):
    """This method divides two numbers with arbritary precision
        number must be smaller than divisor
        returns digits as np.array"""
        
        #stores the digits
    result=np.array([0]*precision)
        #to prevent the first shift with a zero
    number*=10
    index=0
        #do work
    while index<precision:
        if divisor>number:
            number*=10
            index+=1
        else:
                #store the digit
            result[index]=number//divisor
            number-=result[index]*divisor
    
    return result


def solveProblem(limit=1000):
    maxCycle=0
    maxNumber=0
    maxDivisor=0
    for i in range(1,1000):
        number=division(1, i)
        cycleLength=findReoccuring(number)

        if maxCycle<cycleLength:
            maxCycle=cycleLength
            maxNumber=number
            maxDivisor=i
                #debugging
            # print("Nex Max! 1/%d, length=%d" %(i,maxCycle))

    return maxDivisor

print(solveProblem())

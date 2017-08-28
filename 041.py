#!/usr/bin/env python


"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from eulerfunctions import isPrime, isPandigital


def createNumbersRecursive(base, numbers, generatedNumbers):
    """
    This function creates all permutations of a number of concatenated elements of parameter numbers
    """
    numbersForLoop=numbers.copy()
    for digit in numbersForLoop: 
        numbers.remove(digit)
        base=appendDigit(base, digit)
       
        if len(numbers)>0:
            createNumbersRecursive(base, numbers, generatedNumbers)
        else:
            generatedNumbers.append(base)
        
        base=removeDigit(base, digit)
        numbers.append(digit)

    return 

def createNumbers(numbers):
    allNumbers=[]
    createNumbersRecursive(0, numbers,allNumbers) 
    return allNumbers

def appendDigit(number, newDigit):
    return number*10+newDigit

def removeDigit(number, digitToRemove):
    return int((number-digitToRemove)//10)




def solveProblem():
    max = 0
    
    for j in range(1,10):
        numbers=createNumbers([i for i in range(1,j+1)])
        
        for n in numbers:
            if isPrime(n) and n>max:
                max = n

    return max 

print(solveProblem())

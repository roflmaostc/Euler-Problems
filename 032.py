#!/usr/bin/env python

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


def createNumbersRecursive(base, numbers, generatedNumbers):
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
    allPermutations=[]
    createNumbersRecursive(0,[1,2,3,4,5,6,7,8,9],allPermutations)
    
    results=[]
    
    for number in allPermutations:
        # print(number)
        pandigital, result=findPandigital(str(number))
        if pandigital ==True and result not in results:
            results.append(int(result))

    return sum(results)

def findPandigital(number):
    for pos1 in range(1, len(number)-1):
        for pos2 in range(pos1+2, len(number)):
            factor1=int(number[0:pos1])
            factor2=int(number[pos1:pos2])
            result=factor1*factor2
            if(result == int(number[pos2:])):
                return True, result
    return False,0


def listProduct(liste):
    product=1
    for entry in liste:
        product*=entry
    return product

print(solveProblem())


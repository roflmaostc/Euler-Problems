#!/usr/bin/env python
"""
Commonly and often used Euler functions
"""


from math import sqrt

def isPrime(number):
    import numpy as np
    if number==1:
        return False
    if number==2 or number==3:
        return True
    if number%2==0:
        return False
    if number % 3 == 0:
        return False
    for i in range(3, int(np.sqrt(number)//1)+1,2):
        if number%i==0:
            return False
    return True


def isPandigital(number,n):
    #slower than is_pandigital
    s = str(number)
    for i in range(1,n+1):
        if str(i) not in s:
            return False
        s = s.replace(str(i),"",1)
        if str(i) in s:
            return False
    return True


def is_square(apositiveint):
    #from https://stackoverflow.com/a/2489519
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def is_pandigital(num, digits):
    s = str(num)

    for i in digits:
        if str(i) not in s:
            return False

    return True


def is_pandigital2(num, digitsA):
    #slower than is_pandigital
    #digitsA is e.g. 54321
    res = 0
    while num>=1:
        digit = num%10
        num //= 10
        res += 10**(digit-1)*digit 

    return res == digitsA



def rec_pandigital(base, numbers, generatedNumbers):
    """
    This function creates all permutations of a number of concatenated elements of parameter numbers
    """
    numbersForLoop=numbers.copy()
    for digit in numbersForLoop: 
        numbers.remove(digit)
        base=appendDigit(base, digit)
       
        if len(numbers)>0:
            rec_pandigital(base, numbers, generatedNumbers)
        else:
            generatedNumbers.append(base)
        
        base=removeDigit(base, digit)
        numbers.append(digit)
    return  

def create_pandigitals(numbers):
    allNumbers=[]
    rec_pandigital(0, numbers,allNumbers) 
    return allNumbers

def appendDigit(number, newDigit):
    return number*10+newDigit

def removeDigit(number, digitToRemove):
    return int((number-digitToRemove)//10)



def is_pentagonal(p):
   return (1+sqrt(1+24*p))/6%1==0


def is_triangle_number(num):
    #you can rearrange the triangle equation and you will see this is enough
    #use of p-q equation
    return is_square(1+8*num) 


def is_hexagonal(h):
    return (1+sqrt(1+8*h)) % 4 == 0

#!/usr/bin/env python

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import time

def checkIfPalindrome(number):
    number=str(number)
    for i in range(0, len(number)//2):
        if number[i]!=number[-i-1]:
            return False
    return True


def checkIfPalindrome2(number):
    if number/int(str(number)[::-1])==1:
        return True
    return False


def createPal():
    number="1"
    for i in range(1000000):
        number+="1"
    return int(number)


def toBinary(number):
    binary=''
    while number>0:
        if number%2==1:
            binary+='1'
        else:
            binary+='0'
        number//=2
    return int(binary[::-1])


def solveProblem(limit=int(1e6)):
    all=[]
    for number in range(1,limit):
        if checkIfPalindrome(number) and checkIfPalindrome(toBinary(number)):
            all.append(number)

    return sum(all)

print(solveProblem())

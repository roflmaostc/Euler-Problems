#!/usr/bin/env python3

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

def checkIfPalindromic2(number):
    string=str(number)
    return string==string[::-1]

def checkIfPalindromic(number):
    digits=splitNumberIntoList(number)
    
    length=len(digits)
    for i in range(0,length//2):
        if digits[i] != digits[-i-1]:
            return False
    return True


def splitNumberIntoList(number):
    """This function splits a number into a list.
        E.g.: 123456789 -> [1,2,3,4,5,6,7,8,9]
    """
    #list for digits
    digits=[]
    
    #get digits of numner
    while number>0:
        digits.append(number%10)
        number//=10
    
    digits.reverse()
    return digits


def searchPalindromicProduct(order):
    #border of numbers
    start=int(1*10**order)
    end=int(1*10**(order+1))
    numbers=[i for i in range(start, end)]
    
    palindromes=[]
    max=(0,0,0)
    #iterate over the matrix. But only half upper matrix. Not the whole one
    numbersReverse=numbers[::-1]
    for i in numbersReverse:
        for j in numbers[:i-1-10**order]:
            #if palindromic -> append
            if (checkIfPalindromic2(j*i)):
                palindromes.append((i,j,i*j))
                # if(i*j>max[2]):
                #     max=(i,j,i*j)
                # if j<max[1] and i<max[0]:
                #         print("blub")
                #     return palindromes

    return palindromes

def findMaxPalindrome(palindromes):
    """Find maximum number in a palindromic tupel"""
    maxima=max(palindromes, key=lambda tupel:tupel[2])
    return maxima

start=time.time()
print(findMaxPalindrome(searchPalindromicProduct(2)))
print(time.time()-start)

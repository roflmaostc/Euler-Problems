#!/usr/bin/env python

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def numberToWords(number):
    """Returns the number in words"""
    number=str(number)
        #10^power; order of number 
    power=len(number)-1 
    
    word=""
    while power>=0:
        wordAdd, power=digitToWord(str(number),power)
        word+=wordAdd

    return word

def digitToWord(number, power):
        #single numbers

    digit=int(number[len(number)-power-1])

    if power==0:
        digitsWordsConnection={0:"",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
        return digitsWordsConnection[digit], -1
        
        #single numbers inside [10,19]
    elif power==1 and digit==1:
        digitsWordsConnection={0:"ten",1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}
        return digitsWordsConnection[int(number[len(number)-power])], -1

        #single number inside [20,99
    elif power==1:
        digitsWordsConnection={0:"", 1:"ten" ,2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
        return digitsWordsConnection[digit], 0
        
    elif power==2:
        digitsWordsConnection={0:"",1:"onehundred", 2:"twohundred", 3:"threehundred", 4:"fourhundred", 5:"fivehundred", 6:"sixhundred", 7:"sevenhundred", 8:"eighthundred", 9:"ninehundred"}
        if number[-2]=="0" and number[-1]=="0":
            return digitsWordsConnection[digit],1 
        else:
            return digitsWordsConnection[digit]+"and",1 
    elif power==3 and number[1:]=="000":
        return "onethousand",-1

def solveProblem(border=1000):
    allNumbers=""
    for i in range(1, border+1):
        allNumbers+=numberToWords(i)
        print(numberToWords(i))
    return len(allNumbers)

print(solveProblem())

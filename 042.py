#!/usr/bin/env python

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
"""

from math import sqrt
from eulerfunctions import is_square


def wordToNumber(w):
    s = 0
    for c in w:
        #uppercase letters
        s += ord(c)-64
    return s


def extractWords(f):
    with open(f, 'r') as f:
        data = f.read().replace("\"","").split(",")
    return data

def is_triangle_number(num):
    #you can rearrange the triangle equation and you will see this is enough
    #use of p-q equation
    return is_square(1+8*num) 


def solveProblem():
    words = extractWords("files/p042_words.txt")
    counter = 0
    for w in words:
        if is_triangle_number(wordToNumber(w)):
            counter +=1
    
    return counter

print(solveProblem())

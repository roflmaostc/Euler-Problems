#!/usr/bin/env python


"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""

def loadNames(filename):
    """This method loads the file into a sorted list of names"""
        #extract data
    with open(filename) as file:
        data=file.readlines()
    
        #convert into list
    names=data[0].split(",")
    for i in range(len(names)):
        names[i]=names[i][1:-1]
        
    names.sort()
    return names


def solveProblem(names):
    """solves the problem"""
    return sum([alphabeticalValue(name)*i for name,i in zip(names, range(1,len(names)+1))])


def alphabeticalValue(name):
    """Returns the alphabeticalValue as defined in the task"""
    return sum([letterToValue(char) for char in name])


def letterToValue(char):
    """Returns for a "a" a 1 and for "z" a 26"""
    return ord(char.lower())-96

print(solveProblem(loadNames("files/names.txt")))

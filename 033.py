#!/usr/bin/env python

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""



def findCuriousFraction(limit=100, diff=1e-5):
    fractions=[]
    for numerator in range(10,limit):
        for denominator in range(numerator+1,limit):
            numerator=str(numerator)
            denominator=str(denominator)
            if denominator[1]!="0" and numerator[1]!="0":
                if denominator[0]==numerator[0] and denominator[1]!="0" and abs(int(numerator)/int(denominator) - int(numerator[1])/int(denominator[1]))<diff:
                    fractions.append((numerator,denominator))
                    # print("first"+str(numerator)+"/"+str(denominator))
                if denominator[1]==numerator[1] and abs(int(numerator)/int(denominator) - int(numerator[0])/int(denominator[0]))<diff:
                    fractions.append((numerator,denominator))
                    # print("second"+str(numerator)+"/"+str(denominator))
                if denominator[0]==numerator[1] and denominator[1]!="0" and abs(int(numerator)/int(denominator) - int(numerator[0])/int(denominator[1]))<diff:
                    fractions.append((numerator,denominator))
                    # print("third"+str(numerator)+"/"+str(denominator))
                if denominator[1]==numerator[0] and abs(int(numerator)/int(denominator) - int(numerator[1])/int(denominator[0]))<diff:
                    fractions.append((numerator,denominator))
                    # print("fourth"+str(numerator)+"/"+str(denominator))
    return fractions 

def lowerCommonTerms(terms):
    numerator=1
    denominator=1
    for element in terms:
        numerator*=int(element[0])
        denominator*=int(element[1])

    return numerator, denominator


def solveProblem(fraction):
    if fraction[1]%fraction[0]==0:
        return fraction[1]/fraction[0]

print(solveProblem(lowerCommonTerms(findCuriousFraction())))

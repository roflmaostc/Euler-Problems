#!/usr/bin/env python

"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from eulerfunctions import generate_primes, isPrime

def solveProblem():
    ps = generate_primes(int(1e6))
    
    max = 2
    maxIndex = 0
    for i in range(0, len(ps)):
        index = i
        number = ps[i]
        while number<int(1e6):
            if index+1>=len(ps):
                break
            index += 1
            number += ps[index]
            if isPrime(number) and (index-i+1)>maxIndex:
                max = number
                maxIndex = index-i+1
    
    return max



print(solveProblem())

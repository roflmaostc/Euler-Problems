#!/usr/bin/env python
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

from eulerfunctions import isPrime
def new_number(n):
    return n*(n+1)*4


def create_diagonals(n):
    lu = [1+4*(i+1)+new_number(i) for i in range(n)]
    ru = [1+2*(i+1)+new_number(i) for i in range(n)]
    rd = [1+8*(i+1)+new_number(i) for i in range(n)]
    ld = [1+6*(i+1)+new_number(i) for i in range(n)]

    return [1]+lu+ru+rd+ld




def solve():
    diagonals = create_diagonals(100000)
    diagonals.sort()
    
    total = 1 
    primes = 0 
    i = 1 
    while True:
        l_new = list(filter(lambda x: isPrime(x), diagonals[1+4*(i-1):1+4*i]))
        total += 4
        primes += len(l_new)
        ratio = primes/total
        # print(i," ", ratio)
        if ratio<0.1:
            return 2*i+1
        i += 1
    return 0

print(solve())

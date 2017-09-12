#!/usr/bin/env python


"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""


from eulerfunctions import isPrime , generate_primes, prime_factors


def solveProblem():
    ps = generate_primes(int(1e5))

    for i in range(2,int(1e7)):
        for j in [0,1,2,3]:
            if len(prime_factors(i+j, primes = ps, duplicate=False)) != 4:
                break
            if j == 3:
                return i
    return 0

print(solveProblem())

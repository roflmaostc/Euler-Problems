#!/usr/bin/env python
"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from eulerfunctions import generate_primes 

from bitarray import bitarray
import numpy as np

def solveProblem():
    ps = generate_primes(int(1e6))
    primes = create_prime_array(int(1e6), ps)
       
    for number in ps:
        if number < 100000:
            continue
        
        for pos in reversed(range(1,len(str(number))+1)):
            counter = 0
            for d in range(0,10):
                if d==0 and pos == len(str(number)):
                    continue
                if primes[replace_digit(number, d, [pos])]:
                    counter +=1
                    # print(replace_digit(number,d,[pos]))
            if counter == 8:
                return number
            
            for pos2 in reversed(range(1,pos+1)):
                counter = 0
                for d in range(0,10): 
                    if d==0 and pos == len(str(number)):
                        continue
                    if primes[replace_digit(number, d, [pos,pos2])]:
                        counter +=1
                if counter == 8:
                    return number if pos!=len(str(number)) else replace_digit(number,1,[pos,pos2]) 
                
                for pos3 in reversed(range(1,pos2+1)):
                    counter = 0
                    for d in range(0,10): 
                        if d==0 and pos == len(str(number)):
                            continue
                        if primes[replace_digit(number, d, [pos,pos2,pos3])]:
                            counter +=1
                            print(replace_digit(number,d,[pos,pos2,pos3]))
                    if counter == 8:
                        return number if pos!=len(str(number)) else replace_digit(number,1,[pos,pos2,pos3]) 
                        # return number

    return 0

def check_if_fulfilled(number,list, limit):
    for d in range(0,10): 
        if d==0 and pos == len(str(number)):
            continue
        if primes[replace_digit(number, d, [pos,pos2,pos3])]:
            counter +=1
            print(replace_digit(number,d,[pos,pos2,pos3]))
    if counter == limit:
        return number if pos!=len(str(number)) else replace_digit(number,1,[pos,pos2,pos3]) 


def replace_digit(n, d, pos):
    """Replaces digit in number n at all position (stored in pos-list) with digit d"""
    n = str(n)
    
    for p in pos:
        if p>len(n):
            raise ValueError("Position to large for number")
        n = n[:len(n)-p] + str(d) + n[len(n)-p+1:]

    return int(n)


def replace_digit2(n, d, pos):
    """Replaces digit in number n at all position (stored in pos-list) with digit d. Approximately 30% faster than replace_digit. 1023. Digit is 3 is at pos=1 and digit 1 is at pos=4"""
    s = str(n) 
    for p in pos:
        tmp = int(s[p])
        n += 10**(p-1)*(d-tmp)
            
    return n
    
def create_prime_array(limit, ps=[]):
    """Returns a bit array which is at position p true, if p is prime. Otherwise false"""

    if not ps:
        ps = generate_primes(limit)
    pa = bitarray(limit+1)
    pa.setall(False)
    for p in ps:
        pa[p] = True

    return pa


import time

print(solveProblem())


# print(replace_digit2(100000,1, [1]))

# start = time.time()
# for i in range(100,int(1e6)):
    # replace_digit2(100000,0, [1,2,5])
    # replace_digit(100*i,3, [1,2,5])
# print(time.time()-start)

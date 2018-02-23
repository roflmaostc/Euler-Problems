#!/usr/bin/env python
"""
Commonly and often used Euler functions
"""


from math import sqrt

def isPrime(number):
    import numpy as np
    if number==1:
        return False
    if number==2 or number==3:
        return True
    if number%2==0:
        return False
    if number % 3 == 0:
        return False
    for i in range(3, int(np.sqrt(number)//1)+1,2):
        if number%i==0:
            return False
    return True



def prime_factors(n, primes=[], duplicate=True):
    """This function returns a list of prime factors. Can remove duplicate."""
    if not primes:
        primes = generate_primes(int(sqrt(n)//1)+1)
    factors = []
    for p in primes:
        if p*p > n: break 
        while n%p == 0:
            factors.append(p)
            #prevents adding multiple times duplicate
            if duplicate == True:
                n //= p
            else:
                while n%p == 0:
                    n //= p
                break 
    if n > 1:
        factors.append(n)
    return factors


def is_palindrome(x):
    return str(x) == str(x)[::-1]

def reverse(x):
    return int(str(x)[::-1])

def isPandigital(number,n):
    #slower than is_pandigital
    s = str(number)
    for i in range(1,n+1):
        if str(i) not in s:
            return False
        s = s.replace(str(i),"",1)
        if str(i) in s:
            return False
    return True


def is_square(apositiveint):
    #from https://stackoverflow.com/a/2489519
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def is_pandigital(num, digits):
    s = str(num)

    for i in digits:
        if str(i) not in s:
            return False

    return True


def is_pandigital2(num, digitsA):
    #slower than is_pandigital
    #digitsA is e.g. 54321
    res = 0
    while num>=1:
        digit = num%10
        num //= 10
        res += 10**(digit-1)*digit 

    return res == digitsA



def rec_pandigital(base, numbers, generatedNumbers):
    """This function is internally called by create_pandigitals"""
    numbersForLoop=numbers.copy()
    for digit in numbersForLoop: 
        numbers.remove(digit)
        base=appendDigit(base, digit)
       
        if len(numbers)>0:
            rec_pandigital(base, numbers, generatedNumbers)
        else:
            generatedNumbers.append(base)
        
        base=removeDigit(base, digit)
        numbers.append(digit)
    return  

def create_pandigitals(numbers):
    """This function creates all permutations of a number of concatenated elements of parameter numbers
    """
    allNumbers=[]
    rec_pandigital(0, numbers,allNumbers) 
    return allNumbers

def appendDigit(number, newDigit):
    return number*10+newDigit

def removeDigit(number, digitToRemove):
    return int((number-digitToRemove)//10)



def is_pentagonal(p):
   return (1+sqrt(1+24*p))/6%1==0


def is_triangle_number(num):
    #you can rearrange the triangle equation and you will see this is enough
    #use of p-q equation
    return is_square(1+8*num) 


def is_hexagonal(h):
    return (1+sqrt(1+8*h)) % 4 == 0


def gcd(a,b):
    """This function calculatest the greatest common divisor (gcd) by using Euklid's algorithm
    """
    if b>a:
        a,b = b,a
    #assume b<a
    while b != 0:
        h = a%b
        a = b
        b = h
    return a


def generate_primes(limit):
    """This functions creates primes up to a limit using sieve of Erastostehens"""

    limit += 1
    from bitarray import bitarray
    primes = bitarray(limit)
    primes.setall(True)

    #0 and 1 are not primes
    primes[0] = False
    primes[1] = False
    
    #now sieving
    for i in range(2, len(primes)):
        counter = 2*i
        while counter < limit:
            primes[counter] = False 
            counter += i
    
    return [i for i in range(0,limit) if primes[i]]



def factor_number(n):
    """ This algorithm splits a number n into two integers a and b satisfying n = a*b. a and b must not be primes. 
        The used algorithm is Pollard's rho algorithm.
        Doesn't guarantee a solution!"""
   

    if n % 2 == 0 and n != 2:
        return (2, n//2)

    g = lambda x: (x**2+1) % n

    x = 2
    y = 2
    d = 1
    
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = gcd(abs(x-y),n)
    if d == n:
        #number is prime
        return n
    else:
        #one divisor
        return (d,n//d)


def crossfoot(x):
    s = 0
    while x>0:
        s += x%10
        x //= 10
    return s

#!/usr/bin/env python
"""
Commonly and often used Euler functions
"""

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



def isPandigital(number,n):
    s = str(number)
    for i in range(1,n+1):
        if str(i) not in s:
            return False
        s = s.replace(str(i),"",1)
        if str(i) in s:
            return False
    return True


#from https://stackoverflow.com/a/2489519
def is_square(apositiveint):

  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


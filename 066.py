#!/usr/bin/python

"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

"""
Idea: look at wikipedias article about Pell equation
"""
from eulerfunctions import is_square
from math import sqrt, floor

def calc_fraction(a, den=False):
    """if you reverse and cut the last a, you will get denomintaor  
       a+Z/N = (a*N+Z)/N = 1/((a*N+Z)/N)
    """
    if den:
        a = list(reversed(a[:-1]))

    Z = 0
    N = 1
    for ai in a:
        x = ai*N+Z
        oldZ = Z
        Z = N
        N = x
    return Z


def generate_a(n):
    d = dict() 
    a = []
    a0 = floor(sqrt(n))
    a.append(a0)
    S = n
    diff = a0
    N = n-a0**2
    Z = 1
    i = 1

    while True:
        N = N/Z
        Z = 1
        ai = floor( (sqrt(S)+diff)/N)
        diff -= ai*N
        a.append(ai)
        Z = N
        N = S-diff**2
        diff = abs(diff)
        if (Z,N,diff) in d:
            # return i-1
            1 
        else:
            d[(Z,N,diff)] = i

        i += 1
        x = calc_fraction(a) 
        y = calc_fraction(a, den=True)

        if x!=1 and x**2-n*y**2 == 1:
            return x, y

def main():
    r = []
    d = 2
    hm = dict()
    maxx = 0
    maxd = 0
    while d<1001: 
        if is_square(d):
            d += 1 
        x, y = generate_a(d)
        print("d=%d\t\t\t x=%d\t\t\t y=%d\t\t\t 1=%d" %(d,x,y, x**2-d*y**2))
        if x > maxx:
            maxd = d
            maxx = x
        d += 1
    return maxd 

print(main())

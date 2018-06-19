#!/usr/bin/python

"""
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""

def calc_fraction(a):
    """input in reverse: 
       a+Z/N = (a*N+Z)/N = 1/((a*N+Z)/N)
    """
    Z = 0
    N = 1
    for ai in a:
        x = ai*N+Z
        Z = N
        N = x
    return Z

def generate_a(limit):
    a = [2]
    for i in range(1,limit+1):
        if i%3 == 2:
            a.append(2*int(((i+1)/3)))
        else:
            a.append(1)
    return a


def main():
    a = generate_a(100)
    r = [int(i) for i in str(calc_fraction(a))]
    return sum(r)

print(main())

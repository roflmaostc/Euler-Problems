"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
"""

from math import gcd


# Use of Euclid's formula
# add the factor k to generate all triples
def main(Lmax=1500000):
    d = dict()
    # store which triple were already discovered
    seen = dict()
    for m in range(2, 900):
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            k = 1
            L = a + b + c
            a1 = a
            b1 = b
            c1 = c

            while L <= Lmax:
                L = a1 + b1 + c1
                arr = [a1, b1, c1]
                arr.sort()
                a1, b1, c1 = arr

                if L <= Lmax:
                    if (a1, b1, c1) not in seen:
                        seen[(a1, b1, c1)] = True
                        if L not in d:
                            d[L] = 1
                        else:
                            d[L] += 1
                else:
                    break
                k += 1
                a1 = a * k
                b1 = b * k
                c1 = c * k

    counter = 0
    for L in d:
        # print(L, d[L])
        if d[L] == 1:
            counter += 1

    return counter

print(main())


#!/usr/bin/python
"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

from math import factorial



def fac(n):
    res = 0
    n = str(n)
    for d in n:
        res += factorial(int(d))
    return res

def main(n_limit=999999):
    nums = [i for i in range(0, n_limit)]
    nums.reverse()


    final = 0
    seen = dict()
    while nums:
        #get a new number below n_limit
        n = nums.pop()

        counter = 1
        curr = n
        d = {}
        seq = []
        while True:
            # increment the current seq length
            d[curr] = counter
            counter += 1
            #append the number to the seen number 
            seq.append(curr)
            i_fac = fac(curr)
            
            #if endless loop, then break
            if i_fac == curr:
                break

            # if the number occurs again in the same sequence
            if i_fac in d:
                # check if length is 60 and increment
                if abs(d[curr]) == 60 and str(seq) not in seen:
                    seen[str(seq)] = True
                    final += 1
                #break because this seq is processed
                break
            else:
                curr = i_fac

    return final


print(main())

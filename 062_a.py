#!/usr/bin/env python


"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""



#generate permutations. If the prefix of the permutation isn't a prefix of a cube drop it.
def all_permus(nstr, accstr, found, prefhm, hm):
    # print(accstr, nstr, found)
    if len(nstr) == 0:
        if int(accstr) in hm and int(accstr) not in found: 
            return found+[int(accstr)]
        else:
            return found
    else:
        if len(accstr)>0 and int(accstr) not in prefhm:
            return found
        else:
            for i in range(0,len(nstr)):
                found = all_permus(nstr[0:i]+nstr[i+1:], accstr+nstr[i], found, prefhm, hm)
                if len(found) == 5:
                    return found    
    
    return found


def solve():
    #up to 2000
    n = 10000
    #store all cubes and all prefixes to 2000**3
    prefhm = dict()
    hm = dict()

    for i in range(5,n):
        x = str(i**3)
        hm[int(x)] = True
        for j in range(len(x)):
            prefhm[int(x[0:j+1])] = True
   

    for i in range(20,n):
        res = all_permus(str(i**3), "", [], prefhm, hm)
        print(res, i)
        if len(res) == 5:
            return i**3

print(solve())

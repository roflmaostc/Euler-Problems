#!/usr/bin/env python

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from eulerfunctions import generate_primes, isPrime

import itertools as it

def concat_is_p(a,b,hm):
    if (a,b) in hm or (isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))):
        hm[(a,b)] = True
        return True
    return False

def check_numbers(ai,bi,ci,di,ei, p, dic):
    a,b,c,d,e = p[ai], p[bi], p[ci], p[di], p[ei]
    for (x,y) in [(a,b),(a,c),(a,d),(a,e),(b,c),(b,d),(b,e),(c,d),(c,e),(d,e)]:
        if concat_is_p(a,b,dic) == False:
            return ai,bi+1,ci,di,ei 
        if concat_is_p(a,c,dic) == False  or concat_is_p(b,c,dic) == False:
            return ai,bi,ci+1,di,ei 
        if concat_is_p(a,d,dic) == False  or concat_is_p(b,d,dic) == False or concat_is_p(c,d,dic)==False:
            return ai,bi,ci,di+1,ei 
        if concat_is_p(a,e,dic) == False  or concat_is_p(b,e,dic) == False or concat_is_p(c,e,dic)==False or concat_is_p(d,e,dic)==False:
            return ai,bi,ci,di,ei 
        else: 
            return -1,0,0,0,0
        
def adjust_counter(ind, lim):
    for i in range(len(ind)-1):
        if ind[i+1]<=ind[i]:
            ind[i+1] = ind[i]+1
    if ind[0]>=lim: 
        raise ValueError
    
    return ind 

def increment_counter(ind, lim):
    
    def aux(it,prev):
        if len(it)==1:
            return [it[0]+1]
        if len(it)==0:
            return []
        elif it[-1]+1<prev:
            return it[0:-1]+[it[-1]+1]
        else: 
            return aux(it[0:-1],prev-1)+[0]
    return adjust_counter(aux(ind,lim),lim) 


def iterate(limit):
    p = generate_primes(limit)
    #2 and 5 cannot be part of that primes
    p = [p[1]]+[p[3]]+p[4:]
    lim = len(p)
    dic = dict() 
    ind = [0,1,2,3,4]
    i = 0
    while True:
        
        ai,bi,ci,di,ei = increment_counter(ind, lim)
        ind = [ai,bi,ci,di,ei] 
        
        ai,bi,ci,di,ei = check_numbers(ai,bi,ci,di,ei, p, dic)
        ind_ = [ai,bi,ci,di,ei]
        if ai==-1:
            # print(p[ind[0]], p[ind[1]], p[ind[2]],p[ind[3]],p[ind[4]])
            return p[ind[0]]+p[ind[1]]+p[ind[2]]+p[ind[3]]+p[ind[4]] 
        ind = ind_        

print(iterate(10000))

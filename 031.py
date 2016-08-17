#!/usr/bin/env python


import time

def findCoinsRec(value,  counter, last,limit=200):
    for coin in (coin for coin in coins if (coin+value<=limit and coin>=last)):
        if value+coin==limit:
            counter+=1
        elif value+coin<limit:
            counter=findCoinsRec(value+coin, counter, coin, limit)
    return counter
    
def solveProblem():
    return findCoinsRec(0,0,1, 200)

coins=[1,2,5,10,20,50,100,200]
# start=time.time()
print(solveProblem())
# print(str(time.time()-start))

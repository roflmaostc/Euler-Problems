#!/usr/bin/env python

def solveProblem(border=1000):
    list=[0]*1000
    for i in range(1,border+1):
        list[i-1]=i**i
    return str(sum(list))[-10:]

print(solveProblem())

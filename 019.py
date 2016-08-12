#!/usr/bin/env python

"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

"""
Explanation of my solution.
weekday is substituted by numbers:0 Monday, 1 Tuesday, 2 wednesday, 3 thursday, 4 friday, 5 saturday, 6 sunday
"""
def dayNextFirstMonth(weekday, month, year):
    """This method returns the weekday of the first day in a month in dependency on month and year. But you have to give the first weekday of the previous month"""
    if month-1 in [1,3,5,7,8,10,12,0]:
        return (weekday+31)%7
    if month-1 in [4,6,9,11]:
        return (weekday+30)%7
    if month-1==2:
        if year%4==0 and (year%100!=0 or year%400==0):
            print("lap year %d"%year)
            return (weekday+29)%7
        else:
            return (weekday+28)%7


def solveProblem():
        #initial setup
    firstWeekday=0
    day=firstWeekday
    counter=0

    #simulate the first year without counting sundays
    for month in range(2,13):
            day=dayNextFirstMonth(day, month, 1900)
    
        #now iterate over years
    for year in range(1901, 2001):
            #iterate over month
        for month in range(1,13):
            day=dayNextFirstMonth(day, month, year)
            if day == 6:
                counter+=1
    return counter

print(solveProblem())

#!/usr/bin/env python

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""



#MY SOLUTION IDEA
#I solve the problem from bottom to top. You start in the second last line and look which of the belows nodes is better. You add both numbers and do this procedure for alle the nodes in one line.
#Continue with the next line and add again the previous some to the current node sum
def loadTriangleToList(filename):
    """Converts the triangle txt into a list"""
        #read file
    with open(filename) as file:
        data = file.readlines()
        
        #convert data into 2d-list
    list=[[int(i) for i in entry.split()] for entry in data]
    return list


def bottomToTop(triangle):
    nodeSum=triangle
    i=len(triangle)-2
    while i>=0:
        for j in range(i+1):
            nodeSum[i][j]+=maxValueOfKids(nodeSum,i,j)
        i-=1
    return nodeSum[0][0]

def maxValueOfKids(triangle, i,j):
    left=triangle[i+1][j]
    right=triangle[i+1][j+1]
    if left>right:
        return left
    else:
        return right

#OLD PART

def nextNodes(x,y):
        return [y+1,x],[y+1,x+1]


def valueAtNode(point,triangle):
    """Returns the value of a node.
       Point is a tuple of x and yy (y,x). Triangle is the list of
    """
    return triangle[point[0]][point[1]]

def dumbMethod(triangle):
    """This method is just for fun and chooses always the biggest neighbour"""
    way=[0]*len(triangle)
    
    x=0
    y=0

    for i in range (0, len(triangle)-1):
        a,b=nextNodes(x,y)
        if valueAtNode(a, triangle)>valueAtNode(b, triangle):
            y,x=a[0],a[1]
            way[i]=valueAtNode(a, triangle)
        else:
            y,x=b[0],b[1]
            way[i]=valueAtNode(b, triangle)

        
    return sum(way)
#OLD PART END

print(bottomToTop(loadTriangleToList("files/triangle.txt")))

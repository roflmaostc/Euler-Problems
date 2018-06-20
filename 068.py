#!/usr/bin/python

"""
Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
"""


#is field valid
def valid(field, S, cnt):
    if cnt<=8:
        if field[0] + field[1] + field[5] > S:
            return False
        if field[1] + field[2] + field[6] > S:
            return False
        if field[3] + field[2] + field[7] > S:
            return False
        if field[4] + field[3] + field[8] > S:
            return False
        if field[9] + field[4] + field[0] > S:
            return False
    else:
        if field[0] + field[1] + field[5] == S and \
           field[1] + field[2] + field[6] == S and \
           field[3] + field[2] + field[7] == S and \
           field[4] + field[3] + field[8] == S and \
           field[9] + field[4] + field[0] == S:
            return True
        else:
            return False
    return True

#solve for restricted sum
def solve(S, nums, field, cnt, solved):
    for n in nums:
        # print(field)
        field[cnt] = n
        if valid(field, S, cnt):
            if cnt == 9: 
                solved.append(change_format(field))
            else:
                nums.remove(n)
                solve(S, nums, field, cnt+1, solved)
                field[cnt] = 0
                nums.append(n)
                nums.sort()
        
        field[cnt] = 0
    return 

def change_format(s):
    out = [0 for i in range(15)]
    out[0] = s[5] 
    out[1] = s[0] 
    out[2] = s[1] 
    out[3] = s[6] 
    out[4] = s[1] 
    out[5] = s[2] 
    out[6] = s[7] 
    out[7] = s[2] 
    out[8] = s[3] 
    out[9] = s[8] 
    out[10] = s[3] 
    out[11] = s[4] 
    out[12] = s[9] 
    out[13] = s[4] 
    out[14] = s[0] 

    min = 10
    minindex = 0
    for i in range(5):
        if out[3*i]<min:
            minindex = 3*i
            min = out[3*i]
    return out[minindex:]+out[:minindex]


def main():
    field = [0 for i in range(1,11)]
    ns = [i for i in range(1,11)]
    sols = []
    for k in range(14,22):
        solve(k, ns, field, 0, sols) 
    
    sols.sort()
    print(sols)
    n = int(''.join(str(e) for e in sols[-1]))
    return n

print(main())

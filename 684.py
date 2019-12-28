"""
Define s(n) to be the smallest number that has a digit sum of n. For example s(10)=19.
Let S(k)=∑n=1ks(n). You are given S(20)=1074

.

Further let fi
be the Fibonacci sequence defined by f0=0,f1=1 and fi=fi−2+fi−1 for all i≥2

.

Find ∑i=290S(fi)
. Give your answer modulo 1000000007.
"""


# creates array with fibonacci numbers
def create_fibs(n):
    arr = [0 for n in range(n + 1)]
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr

# just for illustration left here
def s(n):
    j = n // 9
    r = n % 9
    return (1 + r) * 10 ** j - 1 


# the sums can be analytically derived from s(n)
def S(n, m):
    # print(n)
    j = n // 9 
    r = n % 9
    
    #offset due to summation
    res = - 14
    res += 5 * pow(10, (j + 1), mod=m) - 9 * j
    
    z = pow(10, j, mod=m)
    for i in range(r + 1, 9):
        res -= (1 + i) * z - 1
    return res % m


def main(n=90, m=1000000007):
    fibs = create_fibs(n=n)
    return sum([S(fibs[i], m) for i in range(2, n + 1)]) % m

print(main())

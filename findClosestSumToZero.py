import sys
import math

def findClosestSumToZero(a):
    a.sort()
    l = 0
    r = len(a) - 1
    closestSum = sys.maxint
    p, q = 0, 0
    while l < r:
        if abs(a[r] + a[l]) < closestSum:
            closestSum = abs(a[r] + a[l])
            p, q = l, r
        if a[r] + a[l] < 0:
            l += 1
        else:
            r -= 1
    return (closestSum, a[p], a[q])

a = [1, 60, -10, 70, -80, 85, -1]
print findClosestSumToZero(a)


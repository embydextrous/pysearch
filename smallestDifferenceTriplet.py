'''
Three arrays of same size are given. Find a triplet such that maximum - minimum in that triplet is minimum of all 
the triplets. A triplet should be selected in a way such that it should have one number 
from each of the three given arrays.

If there are 2 or more smallest difference triplets, then the one with the smallest sum of its elements should be 
displayed.

Examples :

Input : arr1[] = {5, 2, 8}
    arr2[] = {10, 7, 12}
    arr3[] = {9, 14, 6}
Output : 7, 6, 5

Input : arr1[] = {15, 12, 18, 9}
    arr2[] = {10, 17, 13, 8}
    arr3[] = {14, 16, 11, 5}
Output : 11, 10, 9
'''
import sys

def findTriplets(a, b, c, n):
    a.sort()
    b.sort()
    c.sort()
    i = j = k = 0
    minDiff = sys.maxint
    p = q = r = 0
    while i < n and j < n and k < n:
        maxi = max(a[i], b[j], c[k])
        mini = min(a[i], b[j], c[k])
        if maxi - mini < minDiff:
            p, q, r = i, j, k
            minDiff = maxi - mini
        if a[i] == mini:
            i += 1
        if b[j] == mini:
            j += 1
        if c[k] == mini:
            k += 1
    return (max(a[p], b[q], c[r]), a[p] + b[q] + c[r] - max(a[p], b[q], c[r]) - min(a[p], b[q], c[r]), min(a[p], b[q], c[r]))

arr1 = [5, 2, 8] 
arr2 = [10, 7, 12] 
arr3 = [9, 14, 6] 
n = len(arr1) 
print findTriplets(arr1, arr2, arr3, n)


    
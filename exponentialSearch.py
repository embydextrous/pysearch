# Useful for binary search if array size is too large
import time

def exponentialSearch(a, x):
    n = len(a)
    if a[0] == x:
        return 0
    i = 1
    while i < n and a[i] < x:
        i *= 2
    return binarySearch(a, i / 2, min(i, n), x)

def binarySearch(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r-l) / 2
    if a[mid] == x:
        return mid
    if a[mid] > x:
        return binarySearch(a, l, mid - 1, x)
    return binarySearch(a, mid + 1, r, x)

a = [i for i in range(10000000)]
start = time.time()
print exponentialSearch(a, 93988)
print (time.time() - start) * 1000
    
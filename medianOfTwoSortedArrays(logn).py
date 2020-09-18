def median2(a, b):
    return (a + b) / 2.0

def median3(a, b, c):
    return (a + b + c - min(a, b, c) - max(a, b, c))

def median4(a, b, c, d):
    return (a + b + c + d - min(a, b, c, d) - max(a, b, c, d)) / 2.0

def median(arr, n):
    if n == 0:
        return -1
    if n % 2 == 0:
        return (arr[n/2] + arr[n/2 + 1]) / 2.0
    return arr[n/2]

def findMedianUtil(a, b, n, m):
    print a, b, n, m
    if m == 0:
        return median(a, n)
    if m == 1:
        if n == 1:
            return median2(a[0], b[0])
        if n % 2 == 1:
            return median2(a[n/2], median3(a[n/2-1], b[0], a[n/2] + 1))
        return median3(b[0], a[n/2], a[n/2-1])
    if m == 2:
        if n == 2:
            return median4(a[0], a[1], b[0], b[1])
        if n % 2 == 1:
            return median3(a[n/2], max(a[n/2-1], b[0]), min(a[n/2+1], b[1]))
        return median4(a[n/2], a[n/2 - 1], max(b[0], a[n/2 - 2]), min(b[1], a[n/2 + 1]))
    idxA, idxB = (n - 1) / 2, (m - 1) / 2
    if a[idxA] <= b[idxB]:
        return findMedianUtil(a[idxA:], b, n/2 + 1, m - idxB)
    return findMedianUtil(a, b[idxB:], n/2+1, m - idxB)

    

def findMedian(a, b):
    n, m = len(a), len(b)
    if n >= m:
        return findMedianUtil(a, b, n, m)
    else:
        return findMedianUtil(b, a, m, n)

a = [1, 2, 4, 5, 6]
b = [0, 2, 4, 5, 6, 7]
print findMedian(a, b)
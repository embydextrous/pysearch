def findCeiling(a, x):
    n = len(a)
    if n == 0:
        return -1
    if x <= a[0]:
        return a[0]
    if x > a[n-1]:
        return -1
    return a[ceil(a, 0, n - 1, x)]

def ceil(a, l, r, x):
    if l > r:
        return
    m = l + (r-l) / 2
    if a[m] == x:
        return m
    if m > l and a[m] > x and a[m-1] < x:
        return m
    if m < r and a[m] < x and a[m+1] > x:
        return m + 1
    if a[m] < x:
        return ceil(a, m+1, r, x)
    return ceil(a, l, m - 1, x)

a = [1, 3, 4, 6, 8, 9, 10]
for i in range(12):
    print findCeiling(a, i)

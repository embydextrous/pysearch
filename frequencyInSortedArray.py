def findFrequency(a, x):
    n = len(a)
    if n == 0:
        return 0
    r = getRightIndex(a, 0, n - 1, x)
    l = getLeftIndex(a, 0, n - 1, x)
    if l == -1 or r == -1:
        return 0
    return r - l + 1

def getRightIndex(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if l == r and a[r] == x:
        return r
    if mid < r and a[mid] == x and a[mid + 1] > x:
        return mid
    if mid < r and a[mid] == x and a[mid + 1] == x:
        return getRightIndex(a, mid + 1, r, x)
    if a[mid] < x:
        return getRightIndex(a, mid + 1, r, x)
    return getRightIndex(a, l, mid - 1, x)

def getLeftIndex(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if l == r and a[r] == x:
        return r
    if mid > l and a[mid] == x and a[mid - 1] < x:
        return mid
    if mid > l and a[mid] == x and a[mid - 1] == x:
        return getLeftIndex(a, l, mid - 1, x)
    if a[mid] < x:
        return getRightIndex(a, mid + 1, r, x)
    return getLeftIndex(a, l, mid - 1, x)

a = [1, 2, 2, 3]
for i in range(5):
    print findFrequency(a, i)
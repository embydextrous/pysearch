def findFrequency(a, x):
    n = len(a)
    if n == 0:
        return 0
    r = getRightIndex(a, 0, n - 1, x)
    if r == -1:
        return 0
    l = getLeftIndex(a, 0, n - 1, x)
    if l == -1:
        return 0
    return r - l + 1

def getRightIndex(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if (mid == len(a)-1 or x < a[mid+1]) and a[mid] == x:
        return mid
    if x < a[mid]:
        return getRightIndex(a, l, mid - 1, x)
    return getRightIndex(a, mid + 1, r, x)

def getLeftIndex(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if (mid == 0 or x > a[mid-1]) and a[mid] == x:
        return mid
    if x > a[mid]:
        return getLeftIndex(a, mid + 1, r, x)
    return getLeftIndex(a, l, mid - 1, x)

a = [1, 2, 2, 2, 2, 2, 3]
for i in range(5):
    print findFrequency(a, i)
def findAPairWithAGivenDifference(a, d):
    a.sort()
    l, r = 0, len(a) - 1
    for i in a:
        idx = binarySearch(a, l, r, d + i)
        if idx != -1:
            return (i, a[idx])
    return None

def binarySearch(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if a[mid] == x:
        return mid
    if a[mid] > x:
        return binarySearch(a, l, mid - 1, x)
    return binarySearch(a, mid + 1, r, x)


a = [-1, 20, 3, 2, 50, 77]
d = 30
print findAPairWithAGivenDifference(a, d)
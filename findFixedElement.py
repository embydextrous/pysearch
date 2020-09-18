def findFixedElement(a, l, r):
    if l > r:
        return -1
    mid = l + (r-l) / 2
    if a[mid] == mid:
        return mid
    return findFixedElement(a, mid + 1, r) 
    return findFixedElement(a, l, mid -1)


a = [-10, -1, 0, 2, 6, 6, 6, 7, 8]
print findFixedElement(a, 0, len(a) - 1)
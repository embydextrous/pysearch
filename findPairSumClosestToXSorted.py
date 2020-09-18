def findPairSumClosestToX(a, x):
    l, r = 0, len(a) - 1
    i, j = -1, -1
    closestToX = abs(a[r] + a[l] - x)
    while l < r:
        if a[l] + a[r] - x == 0:
            return (l, r)
        if closestToX > abs(a[l] + a[r] - x):
            closestToX = abs(a[l] + a[r] - x)
            i, j = l, r
        if a[l] + a[r] - x > 0:
            r -= 1
        else:
            l += 1
    return (i, j)

a = [10, 22, 28, 29, 30, 40]
print findPairSumClosestToX(a, 54)
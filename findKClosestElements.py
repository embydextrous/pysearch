def findKClosest(a, k, x):
    n = len(a)
    if x <= a[0]:
        return a[:k]
    if x >= a[n-1]:
        return a[n-k:]
    c = findCrossover(a, 0, n-1, x)
    l, r = max(c-k, 0), min(c+k, n - 1)
    while r - l + 1 != k:
        if a[r] - x <= x - a[l]:
            l += 1
        else:
            r -= 1
    return a[l:r+1]

def findCrossover(a, l, r, x):
    if l > r:
        return -1
    m = l + (r-l) / 2
    if a[m] == x:
        return m
    if a[m-1] < x and a[m] > x:
        return m
    if a[m] > x:
        return findCrossover(a, l, m-1, x)
    return findCrossover(a, m+1, r, x)

a = [1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 21, 24, 26, 28, 30]
for i in range(32):
    print i, " -> ", findKClosest(a, 5, i)
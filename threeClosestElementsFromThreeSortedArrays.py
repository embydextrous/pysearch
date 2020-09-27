import sys

def threeClosestElements(a, b, c):
    minClosest = sys.maxint
    result = None
    for i in a:
        floorB = floor(b, 0, len(b) - 1, i)
        if floorB is None:
            continue
        floorC = floor(c, 0, len(c) - 1, i)
        if floorC is None:
            continue
        closest = abs(floorB - i) + abs(floorC - i) + abs(floorB - floorC)
        if closest < minClosest:
            minClosest = closest
            result = (i, floorB, floorC)
    for i in b:
        floorA = floor(a, 0, len(a) - 1, i)
        if floorA is None:
            continue
        floorC = floor(c, 0, len(c) - 1, i)
        if floorC is None:
            continue
        closest = abs(floorA - i) + abs(floorC - i) + abs(floorA - floorC)
        if closest < minClosest:
            minClosest = closest
            result = (floorA, i, floorC)
    for i in c:
        floorB = floor(b, 0, len(b) - 1, i)
        if floorB is None:
            continue
        floorA = floor(a, 0, len(a) - 1, i)
        if floorA is None:
            continue
        closest = abs(floorB - i) + abs(floorA - i) + abs(floorB - floorA)
        if closest < minClosest:
            result = (floorA, floorB, i)
    return result

def floor(a, l, r, x):
    if l > r or a[l] > x:
        return None
    mid = l + (r - l) / 2
    if a[mid] == x:
        return a[mid]
    if mid > l and a[mid] > x and a[mid - 1] < x:
        return a[mid - 1]
    if mid < r and a[mid] < x and a[mid + 1] > x:
        return a[mid]
    if a[mid] > x:
        return floor(a, l, mid - 1, x)
    return floor(a, mid + 1, r, x)


a = [20, 24, 100]
b = [2, 19, 22, 79, 800] 
c = [10, 12, 23, 25, 119]
print threeClosestElements(a, b, c)

q = [1, 4, 5, 8, 9, 10]
for i in range(12):
    print floor(q, 0, len(q) - 1, i)
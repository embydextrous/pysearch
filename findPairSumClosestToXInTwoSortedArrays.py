def findPairSumClosest(a, b, x):
    c1, c2 = len(a), len(b)
    l1 = l2 = 0
    r1 = c1 - 1
    r2 = c2 - 1
    closestSum = abs(min(a[l1], b[l2]) + max(a[r1], b[r2]) - x)
    p, q = -1, -1
    while l1 <= r1 or l2 <= r2:
        left = min(a[l1], b[l2]) if l1 < c1 and l2 < c2 else a[l1] if l1 < c1 else b[l2]
        right = max(a[r1], b[r2]) if r1 >= 0 and r2 >= 0 else a[r1] if r1 >= 0 else b[r2]
        if left + right == x:
            return (left, right)
        if abs(left + right - x) < closestSum:
            closestSum = abs(left + right - x)
            p, q = left, right
        if left + right - x < 0:
            if left == a[l1]:
                l1 += 1
            if left == b[l2]:
                l2 += 1
        else:
            if right == a[r1]:
                r1 -= 1
            if right == b[r2]:
                r2 -= 1
    return (p, q)

a = [1, 4, 5, 7]
b = [10, 20, 30, 40]

print findPairSumClosest(a, b, 8)
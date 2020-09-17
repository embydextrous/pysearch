def findMaxAndMin(a, n):
    if n == 0:
        return (None, None)
    if n == 1:
        return (a[0], a[0])
    mx, mn, i = 0, 0, 0
    if n % 2 == 0:
        mx, mn = max(a[0], a[1]), min(a[0], a[1])
        i = 2
    else:
        mx = mn = a[0]
        i = 1
    while i < n:
        mx = max(mx, a[i], a[i+1])
        mn = min(mn, a[i], a[i+1])
        i += 2
    return (mx, mn)

a = [10, 2, 8, 12, 7, 1, 6]
print findMaxAndMin(a, len(a))
    

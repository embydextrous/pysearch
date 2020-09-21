def findMaxThree(a):
    if len(a) < 3:
        return None
    l, tl = max(a[0], a[1], a[2]), min(a[0], a[1], a[2])
    sl = a[0] + a[1] + a[2] - l - tl
    for i in range(3, len(a)):
        if a[i] >= l:
            l, sl, tl = a[i], l, sl
        elif a[i] >= sl:
            sl, tl = a[i], sl
        elif a[i] > tl:
            tl = a[i]
    return (l, sl, tl)

a = [3, 6, 1, 9, 7, 8, 5, 8]
print findMaxThree(a)
def interpolationSearch(a, l, r, x):
    if l >= r or x < a[l] or x > a[r]:
        return -1
    pos = l + ((x - a[l]) * (r - l)) / (a[r] - a[l])
    if a[pos] == x:
        return pos
    if a[pos] > x:
        return interpolationSearch(a, l, pos - 1, x)
    return interpolationSearch(a, pos + 1, r, x)

a = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
for i in range(50):
    print i, interpolationSearch(a, 0, len(a) - 1, i)  
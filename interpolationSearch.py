import time

def interpolationSearch(a, l, r, x):
    if l >= r or x < a[l] or x > a[r]:
        return -1
    pos = l + ((x - a[l]) * (r - l)) / (a[r] - a[l])
    if a[pos] == x:
        return pos
    if a[pos] > x:
        return interpolationSearch(a, l, pos - 1, x)
    return interpolationSearch(a, pos + 1, r, x)

a = [i for i in range(10000000)]
start = time.time()
print interpolationSearch(a, 0, 9999999,93988)
print (time.time() - start) * 1000
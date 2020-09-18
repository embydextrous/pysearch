def ceil(a, l, r, x):
    if l > r:
        return -1
    if x <= a[l]:
        return a[l]
    m = l + (r-l) / 2
    if a[m] == x:
        return a[m]
    if m > l and a[m] > x and a[m-1] < x:
        return a[m]
    if m < r and a[m] < x and a[m+1] > x:
        return a[m + 1]
    if a[m] < x:
        return ceil(a, m + 1, r, x)
    return ceil(a, l, m - 1, x)

def floor(a, l, r, x):
    if l > r:
        return
    if x >= a[r]:
        return a[r]
    m = l + (r-l) / 2
    if a[m] == x:
        return a[m]
    if m > l and a[m-1] < x and a[m] > x:
        return a[m - 1]
    if m < r and a[m] < x and a[m+1] > x:
        return a[m]
    if a[m] < x:
        return floor(a, m + 1, r, x)
    return floor(a, l, m - 1, x)

a = [1, 3, 4, 6, 8, 9, 10]
for i in range(12):
    #print ceil(a, 0, len(a) - 1, i)
    print floor(a, 0, len(a) - 1, i)

def linearSearch(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1

def recursiveLinearSearch(a, l, r, x):
    if l > r:
        return -1
    if a[l] == x:
        return l
    if a[r] == x:
        return r
    return recursiveLinearSearch(a, l + 1, r - 1, x)

a = [1, 2, 3, 4, 5]
for i in range(9):
    print linearSearch(a, i)
    print recursiveLinearSearch(a, 0, len(a) - 1, i)
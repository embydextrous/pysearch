def count1InBinarySortedArray(a):
    n = len(a)
    l = first(a, 0, n - 1)
    print l
    if l == -1:
        return 0
    return n - l


def first(a, l, r):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if a[mid] == 1 and (mid == 0 or a[mid-1] == 0):
        return mid
    if a[mid] == 0:
        return first(a, mid + 1, r)
    return first(a, l, mid - 1)


a = [0, 1, 1, 1, 1]
count1InBinarySortedArray(a)


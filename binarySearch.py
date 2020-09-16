def binarySearch(a, l, r, key):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if a[mid] == key:
        return mid
    if a[mid] > key:
        return binarySearch(a, l, mid - 1, key)
    return binarySearch(a, mid + 1, r, key)

a = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(10):
    print binarySearch(a, 0, len(a) - 1, i)


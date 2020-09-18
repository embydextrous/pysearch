def findPeakElement(a, l, r, n):
    if l > r:
        return -1
    mid = l + (r-l) / 2
    if (mid == 0 and a[mid + 1] <= a[mid]) or (mid == n - 1 and a[mid-1] <= a[mid]) or max(a[mid], a[mid+1], a[mid-1]) == a[mid]:
        return a[mid]
    if mid > l and a[mid-1] > a[mid]:
        return findPeakElement(a, l, mid - 1, n)
    return findPeakElement(a, mid + 1, r, n)

a = [1, 3, 20, 4, 1, 0]
n = len(a)
print findPeakElement(a, 0, n - 1, n)
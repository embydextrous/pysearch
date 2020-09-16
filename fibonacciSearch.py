def fibonacciSearch(a, x):
    n = len(a)
    fibm2 = 0
    fibm1 = 1
    fibm = fibm1 + fibm2
    while fibm < n:
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1 + fibm2
    offset = -1
    while fibm > 1:
        i = min(fibm2+offset, n-1)
        if a[i] == x:
            return i
        elif a[i] < x:
            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm - fibm1
            offset = i
        else:
            fibm = fibm2
            fibm1 = fibm1 - fibm2
            fibm2 = fibm - fibm1
    if fibm1 and a[offset+1] == x:
        return offset+1
    return -1

a = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90]
print fibonacciSearch(a, 85)


            
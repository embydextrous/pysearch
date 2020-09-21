class Rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d

def binarySearch(a, l, r, x):
    if l > r:
        return -1
    mid = l + (r - l) / 2
    if a[mid].n == x.n and a[mid].d == x.d:
        return mid
    if a[mid].n * x.d > a[mid].d * x.n:
        return binarySearch(a, l, mid - 1, x)
    return binarySearch(a, mid + 1, r, x)

a = [Rational(2, 3), Rational(3, 4), Rational(4, 5), Rational(1, 1), Rational(6, 5), Rational(7, 5), Rational(13, 9)]
print binarySearch(a, 0, len(a) - 1, Rational(1, 2))
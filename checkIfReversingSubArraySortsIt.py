# Assume that array has distinct integers
def checkIfReversingSubArrayMakesItSorted(a):
    n = len(a)
    if n < 2:
        return True
    p, q = a[0], a[1]
    isNonDecreasing = q >= p
    i = 1
    part = 0
    while i < n - 1:
        p, q = a[i], a[i + 1]
        if isNonDecreasing:
            if q < p:
                isNonDecreasing = False
                part += 1
        else:
            if q > p:
                isNonDecreasing = True
                part += 1
        i += 1
        if part == 3:
            return False
    return True

a = [1, 2, 3, 6, 5, 4, 7, 8]
print checkIfReversingSubArrayMakesItSorted(a)
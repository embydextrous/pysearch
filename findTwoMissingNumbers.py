def findTwoMissing(a, n):
    xor = 0
    for i in a:
        xor ^= i
    for i in range(1, n + 1):
        xor ^= i
    fsb = xor & ~(xor - 1)
    xor1 = xor2 = 0
    for i in a:
        if i & fsb == 0:
            xor1 ^= i
        else:
            xor2 ^= i
    for i in range(1, n + 1):
        if i & fsb == 0:
            xor1 ^= i
        else:
            xor2 ^= i
    return (xor1, xor2)


a = [1, 3, 4, 5, 6, 8]
print findTwoMissing(a, 8)

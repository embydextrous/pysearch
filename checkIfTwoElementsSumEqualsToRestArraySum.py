def check(a):
    n = len(a)
    summ = 0
    for i in a:
        summ += i
    if summ & 1 == 1:
        return None
    summ >>= 1
    s = set()
    for i in a:
        if summ - i in s:
            return (i, summ - i)
        s.add(i)
    return None

a = [2, 11, 5, 1, 4, 7]
print check(a)


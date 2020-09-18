def printNumbers(a, k, n):
    t = n/k + 1
    s = {}
    for i in a:
        if i in s:
            s[i] -= 1
            if s[i] == 0:
                print i,
        else:
            s[i] = t - 1

a = [3, 1, 2, 2, 1, 2, 3, 3]
printNumbers(a, 4, len(a))
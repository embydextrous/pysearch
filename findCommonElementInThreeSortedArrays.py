def printIntersection(a, b, c):
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            print a[i],
            i += 1
            j += 1
            k += 1
        else:
            m = min(a[i], b[j], c[k])
            if m == a[i]:
                i += 1
            if m == b[j]:
                j += 1
            if m == c[k]:
                k += 1

a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]

printIntersection(a, b, c)
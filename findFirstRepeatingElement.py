def findFirstRepeatingElement(a):
    s = {}
    minIndex = len(a)
    for i in range(len(a)):
        if a[i] in s and s[a[i]] < minIndex:
            minIndex = s[a[i]]
        else:
            s[a[i]] = i
    return a[minIndex] if minIndex < len(a) else -1

a = [10, 5, 3, 4, 3, 5, 6]
print findFirstRepeatingElement(a)
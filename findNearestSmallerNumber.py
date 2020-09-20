def findNearestSmaller(a):
    s = []
    result = []
    for i in a:
        minEle = None
        while len(s) > 0:
            q = s[len(s) - 1]
            if q >= i:
                s.pop()
            else:
                minEle = q
                break
        result.append(minEle)
        s.append(i)
    return result

a = [1, 6, 4, 10, 2, 5]
print findNearestSmaller(a)
a = [1, 3, 0, 2, 5]
print findNearestSmaller(a)

        
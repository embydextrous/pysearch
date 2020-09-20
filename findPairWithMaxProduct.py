def findPairWithMaxProduct(a):
    min1 = min(a[0], a[1])         
    min2 = max(a[0], a[1])
    max1 = max(a[0], a[1])
    max2 = min(a[0], a[1])
    for i in range(2, len(a)):
        if a[i] >= max1:
            max1, max2 = a[i], max1
        elif a[i] > max2:
            max2 = a[i]
        if a[i] <= min1:
            min1, min2 = a[i], min[1]
        elif a[i] < min2:
            min2 = a[i]
    if max(min1, min2) < 0 and min(max1, max2) > 0:
        if min1 * min2 >= max1 * max2:
            return (min1, min2)
        else:
            return (max1, max2)
    if max(min1, min2) < 0:
        return (min1, min2)
    if min(max1, max2) > 0:
        return (max1, max2)
    if max(min1, min2) == 0:
        return (min1, min2)
    if min(max1, max2) == 0:
        return (max1, max2)
    return (min2, max2)

a = [-1, 4, 0]
print findPairWithMaxProduct(a)
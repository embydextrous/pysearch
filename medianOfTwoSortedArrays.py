def median(a, b):
    n1, n2 = len(a), len(b)
    p = (n1 + n2) / 2
    l1, l2 = 0, 0
    count = 0
    while count <= p and l1 < n1 and l2 < n2:
        if a[l1] <= b[l2]:
            if count == p:
                if (n1 + n2) % 2 == 0:
                    if l1 + 1 < n1:
                        return (a[l1] + min(a[l1 + 1], b[l2])) / 2.0
                    else:
                        return (a[l1] + b[l2]) / 2.0
                else:
                    return a[l1]
            l1 += 1
        else:
            if count == p:
                if (n1 + n2) % 2 == 0:
                    if l2 + 1 < n2:
                        return (b[l2] + min(b[l2 + 1], a[l1])) / 2.0
                    else:
                        return (a[l1] + b[l2]) / 2.0
                else:
                    return b[l2]
            l2 += 1
        count += 1

    while count <= p and l1 < n1:
        if count == p:
            if (n1 + n2) % 2 == 0:
                return (a[l1] + a[l1 + 1]) / 2.0
            else:
                return a[l1]
        count += 1
        l1 += 1

    while count <= p and l2 < n2:
        if count == p:
            if (n1 + n2) % 2 == 0:
                return (b[l2] + b[l2 + 1]) / 2.0
            else:
                return b[l2]
        count += 1
        l2 += 1


a = [1, 3, 4, 6, 8]
b = [2, 5, 7, 9]

print median(a, b)

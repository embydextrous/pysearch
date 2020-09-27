def findAllTripletsWithZeroSum(a):
    a.sort()
    n = len(a)
    result = []
    s = set()
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            if l == i:
                l += 1
                continue
            if r == i:
                r -= 1
                continue
            summ = a[l] + a[r] + a[i]
            if summ == 0:
                if a[l] in s and a[r] in s and a[i] in s:
                    break
                result.append((a[l], a[r], a[i]))
                s.add(a[i])
                s.add(a[l])
                s.add(a[r])
            if summ < 0:
                l += 1
            else:
                r -= 1
    return result

a = [-3, 1, 2, -2, -3, 4, 5]
print findAllTripletsWithZeroSum(a)
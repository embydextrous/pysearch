def binarySearch(a, l, r, s):
    if l > r:
        return -1
    m = l + (r - l) / 2
    if a[m] == s:
        return m
    if a[m] == "":
        i, j = m - 1, m + 1
        x = None
        while i >= l or j <= r:
            if a[i] != "":
                if a[i] == s:
                    return i
                if a[i] > s:
                    return binarySearch(a, l, i - 1, s)
                else:
                    return binarySearch(a, m + 1, r, s)
            i -= 1
            if a[j] != "":
                if a[j] == s:
                    return j
                if a[j] > s:
                    return binarySearch(a, l, m - 1, s)
                else:
                    return binarySearch(a, l, j + 1, s)
            j += 1
    else:
        if a[m] > s:
            return binarySearch(a, l, m - 1, s)
        else:
            return binarySearch(a, m + 1, r, s)

a = ["for", "", "", "", "geeks", "ide", "", "practice", "" , "", "quiz", "", ""]
print binarySearch(a, 0, len(a) - 1, "modi")
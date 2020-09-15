def linearSearch(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1

a = [1, 2, 3, 4, 5]
for i in range(9):
    print linearSearch(a, i)
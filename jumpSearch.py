import math

def jumpSearch(a, key):
    n = len(a)
    step = int(math.sqrt(n))
    prev, i = 0, step - 1
    while i < n and a[i] <= key:
        prev, i = i, i + step
    for j in range(step):
        if prev + j < n and a[prev + j] == key:
            return prev + j
    return -1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

for i in range(20):
    print jumpSearch(a, i)

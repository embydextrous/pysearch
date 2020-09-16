import sys

# Assuming array length > 2
def findMinAndSecondMin(a):
    m1, m2 = min(a[0], a[1]), max(a[0], a[1])
    for i in a:
        if i < m1:
            m2, m1 = m1, i
        elif i < m2:
            m2 = i
    return (m1, m2)

a = [2, 4, 1, 3, 7, 8, 1, 2]
print findMinAndSecondMin(a)

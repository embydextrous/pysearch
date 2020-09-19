from random import randrange

# Find random number and swap it with first element and find partition
def randomPartition(a, l, r):
    n = r - l + 1
    pivot =  randrange(1, 100) % n
    a[l + pivot], a[l] = a[l], a[l + pivot]
    return partition(a, l, r)

def partition(a, l, r):
    i, j = l + 1, r
    while i <= j:
        while i <= j and a[i] <= a[l]:
            i += 1
        while i <= j and a[j] >= a[l]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j 

def kthSmallest(a, l, r, k):
    if l <= r:
        pos = randomPartition(a, l, r)
        if pos == k - 1:
            return a[pos]
        if pos > k - 1:
            return kthSmallest(a, l, pos - 1, k)
        return kthSmallest(a, pos + 1, r, k)

a = [10, 2, 8, 11, 14, 1, 3, 5, 0, 16, 14, 12, 9]
print sorted(a)
for i in range(1, len(a) + 1):
    print kthSmallest(a, 0, len(a) - 1, i)
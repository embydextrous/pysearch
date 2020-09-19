'''
Note that the algorithm is linear in worst case, but the constants are very high for this algorithm. Therefore, 
this algorithm doesn’t work well in practical situations, randomized quickSelect works much better and preferred.
'''

def kthSmallest(a, l, r, k):
    if l <= r:
        n = r - l + 1
        median = []
        i = 0
        while i < n / 5:
            median.append(findMedian(a, l + i * 5, 5))
            i += 1
        if i * 5 < n:
            median.append(findMedian(a, l + i * 5, n % 5))
            i += 1

        if i == 1:
            medianOfMedian = median[i - 1]
        else:
            medianOfMedian = kthSmallest(median, 0, i - 1, i / 2)

        pos = partition(a, l, r, medianOfMedian)  
        if (pos == k - 1):  
            return a[pos]  
        if (pos > k - 1): 
            return kthSmallest(a, l, pos - 1, k)  
        return kthSmallest(a, pos + 1, r,  k)

def partition(a, l, r, x):
    n = r - l + 1
    for i in range(l, l + n):
        if a[i] == x:
            a[l], a[i] = a[i], a[l]
            break
    i, j = l + 1, r
    while i <= j:
        if i <= j and a[i] <= a[l]:
            i += 1
        if i <= j and a[j] >= a[l]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def findMedian(a, l, n):
    lis = sorted(a[l:l+n])
    return lis[n / 2]

a = [10, 8, 2, 12, 17, 4, 1, 19, 15, 16, 11]
print sorted(a)
for i in range(1, 12):
    print kthSmallest(a, 0, len(a) - 1, i)

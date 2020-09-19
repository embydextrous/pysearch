def buildMaxHeap(a, n):
    for i in range(n/2 - 1, -1, -1):
        maxHeapify(a, n, i)

def buildMinHeap(a, n):
    for i in range(n/2 - 1, -1, -1):
        minHeapify(a, n, i)

def maxHeapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[largest] < a[l]:
        largest = l
    if r < n and a[largest] < a[r]:
        largest = r
    if i != largest:
        a[largest], a[i] = a[i], a[largest]
        maxHeapify(a, n, largest)

def minHeapify(a, n, i):
    smallest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[smallest] > a[l]:
        smallest = l
    if r < n and a[smallest] > a[r]:
        smallest = r
    if i != smallest:
        a[smallest], a[i] = a[i], a[smallest]
        minHeapify(a, n, smallest)

def findKthLargestMinHeap(a, k):
    buildMinHeap(a, k)
    for i in range(k, len(a)):
        if a[i] > a[0]:
            a[i], a[0] = a[0], a[i]
            minHeapify(a, k, 0)
    return a[0]

def findKthLargestMaxHeap(a, k):
    n = len(a)
    buildMaxHeap(a, n)
    for i in range(n-1, n-k-1, -1):
        a[i], a[0] = a[0], a[i]
        maxHeapify(a, i, 0)
    return a[-k]

def findKthSmallestMinHeap(a, k):
    n = len(a)
    buildMinHeap(a, n)
    for i in range(n-1, n-k-1, -1):
        a[i], a[0] = a[0], a[i]
        minHeapify(a, i, 0)
    return a[-k]

def findKthSmallestMaxHeap(a, k):
    buildMaxHeap(a, k)
    for i in range(k, len(a)):
        if a[i] < a[0]:
            a[i], a[0] = a[0], a[i]
            maxHeapify(a, k, 0)
    return a[0]

a = [10, 8, 2, 12, 17, 4, 1, 19, 15, 16, 11]
print sorted(a)
print findKthLargestMinHeap(a, 4)
print findKthLargestMaxHeap(a, 4)
print findKthSmallestMinHeap(a, 4)
print findKthSmallestMaxHeap(a, 4)
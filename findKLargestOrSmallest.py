def minHeapify(a, n, i):
    smallest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[l] < a[smallest]:
        smallest = l
    if r < n and a[r] < a[smallest]:
        smallest = r
    if i != smallest:
        a[i], a[smallest] = a[smallest], a[i]
        minHeapify(a, n, smallest)

def maxHeapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, n, largest)

def buildMaxHeap(a):
    n = len(a)
    last = n / 2 - 1
    for i in range(last, -1, -1):
        maxHeapify(a, n, i)
    
def buildMinHeap(a):
    n = len(a)
    last = n/2 - 1
    for i in range(last, -1, -1):
        minHeapify(a, n, i)

def findKLargest(a, k):
    result = a[:k]
    buildMinHeap(result)
    for i in range(k, len(a)):
        if a[i] > result[0]:
            result[0] = a[i]
            minHeapify(result, k, 0)
    return result

def findKSmallest(a, k):
    result = a[:k]
    buildMaxHeap(result)
    for i in range(k, len(a)):
        if a[i] < result[0]:
            result[0] = a[i]
            maxHeapify(result, k, 0)
    return result


a = [3, 5, 1, 2, 8, 4, 10, 7, 6, 0, 9]
print findKLargest(a, 5)
print findKSmallest(a, 5)

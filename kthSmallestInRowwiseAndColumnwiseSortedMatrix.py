def kthSmallest(a, k, n):
    result = [a[i/n][i%n] for i in range(k)]
    buildMaxHeap(result, k)
    print result
    for i in range(k, n * n):
        if a[i/n][i%n] < result[0]:
            result[0], a[i/n][i%n] = a[i/n][i%n], result[0]
            maxHeapify(result, 0, k)
    return result[0]

def buildMaxHeap(a, k):
    last = k/2 - 1
    for i in range(last, -1, -1):
        maxHeapify(a, i, k)

def maxHeapify(a, i, n):
    largest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, largest, n)
    

a = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
print kthSmallest(a, 7, 4)
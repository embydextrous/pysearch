from random import randrange

def buildMinHeap(a):
    n = len(a)
    for i in range(n/2-1, -1, -1):
        minHeapify(a, n, i)

def minHeapify(a, n, i):
    smallest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[l] < a[smallest]:
        smallest = l
    if r < n and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        minHeapify(a, n, smallest)

result = []
def kthLargest(x, k):
    if len(result) < k:
        result.append(x)
        if len(result) == k:
            buildMinHeap(result)
    else:
        if result[0] < x:
            result[0] = x
            minHeapify(result, k, 0)
    if len(result) == k:
        return result[0]
    return None

inp = []
for i in range(1, 100):
    inp.append(i)

gen = []
while len(inp) > 0:
    x = randrange(1, len(inp))
    gen.append(inp[x])
    print sorted(gen)
    print kthLargest(inp[x], 8)
    inp.remove(inp[x])





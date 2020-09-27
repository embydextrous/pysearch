def minTime(a, m):
    return bs(a, len(a), m, m * max(a))

def bs(a, n, m, high):
    low = 1
    while low < high: 
        mid = (low + high) >> 1
        itm = findItems(a, n, mid) 
        if itm < m: 
            low = mid + 1
        else: 
            high = mid 
    return high 

def findItems(a, n, time):
    items = 0
    for i in range(n):
        items += time/a[i]
    return items

a = [1, 2, 3]
m = 11
print minTime(a, m)

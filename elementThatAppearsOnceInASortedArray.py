'''
Given a sorted array in which all elements appear twice (one after one) and one element appears only once. 
Find that element in O(log n) complexity.

Example:

Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}
Output:  4

Input:   arr[] = {1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8}
Output:  8
'''
def search(a, l, r):
    if l > r:
        return None
    if l == r:
        return a[r]
    mid = l + (r - l) / 2
    if mid % 2 == 0:
        if a[mid] == a[mid+1]:
            return search(a, mid + 2, r)
        else:
            return search(a, l, mid)
    else:
        if a[mid] == a[mid-1]:
            return search(a, mid + 1, r)
        else:
            return search(a, l, mid - 1)


a = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
print search(a, 0, len(a) - 1)
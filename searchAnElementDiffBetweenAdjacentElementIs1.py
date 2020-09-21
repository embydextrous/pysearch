'''
Given an array where difference between adjacent elements is 1, write an algorithm to search for an element in the array 
and return the position of the element (return the first occurrence).

Examples :

Let element to be searched be x

Input: arr[] = {8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3}     
       x = 3
Output: Element 3 found at index 7

Input: arr[] =  {1, 2, 3, 4, 5, 4}
       x = 5
Output: Element 5 found at index 4
'''
def search(a, x):
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        else:
            i += abs(x - a[i])
    return -1

a = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]
print search(a, 1)
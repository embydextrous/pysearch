import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def secondMin(a):
    n = len(a)
    li = []
    i = 0
    while i < n:
        node1 = Node(a[i])
        if i + 1 < n:
            node2 = Node(a[i+1])
            root = Node(a[i]) if a[i] <= a[i+1] + 1 else Node(a[i+1])
            root.left = node1
            root.right = node2
            li.append(root)
            i += 2
        else:
            li.append(node1)
            i += 1
    while len(li) > 1:
        isEvenLength = len(li) % 2 == 0
        last = len(li) - 1 if isEvenLength else len(li) - 2
        i = 0
        while i < last:
            node1 = li.pop(0)
            node2 = li.pop(0)
            root =  root = Node(node1.data) if node1.data <= node2.data + 1 else Node(node2.data)
            root.left = node1
            root.right = node2
            li.append(root)
            i += 2
        if not isEvenLength:
            node = li.pop(0)
            li.append(node)
    mini = li[0].data
    secondMini = findSecondMini(li[0], sys.maxint)
    return (mini, secondMini)

def findSecondMini(root, res):
    if root is None or (root.left is None and root.right is None):
        return res
    if root.left and root.left.data < res and root.left.data != root.data:
        res = root.left.data
        return findSecondMini(root.left, res)
    if root.right and root.right.data < res and root.right.data != root.data:
        res = root.right.data
        return findSecondMini(root.right, res)

a = [3, 6, 100, 9, 10, 12, 7, -1, 1]
print secondMin(a)
        
        





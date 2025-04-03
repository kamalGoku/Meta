'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and
successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor
of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the
tree node should point to its predecessor, and the right pointer should point to its successor.
You should return the pointer to the smallest element of the linked list.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#root = [4,2,5,1,3]
'''
        4
      2   5
    1   3
'''
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

def convertToDLL(root):
    if not root:
        return None
    head = None
    prev = None
    def dfs(root):
        nonlocal head, prev
        if not root:
            return None
        dfs(root.left)
        if prev==None:
            head = root
        else:
            prev.right = root
            root.left = prev
        prev = root
        dfs(root.right)

    dfs(root)
    if head:
        prev.next = head
        head.left = prev
    return head

def printDLL(head):
    curr = head
    while curr:
        print(curr.val, end='->')
        curr = curr.right
        if curr==head:
            break
    print("H", head.val)
    
head = convertToDLL(root)
printDLL(head)


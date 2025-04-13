'''
708. Insert into a Cyclic Sorted List
Given a node from a cyclic linked list which is sorted in ascending order,
write a function to insert a value into the list such that it remains a cyclic sorted list.
The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the
reference to that single node. Otherwise, you should return the original given node.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
'''
           c
3--->4---->1-|
|____________|

p    c
1--->3---->4-|
|____________|
'''
head = Node(3)
head.next = Node(4)
head.next.next = Node(1)
head.next.next.next = head

def insertToList(head, val):
    newNode = Node(val)
    if not head:
        newNode.next = newNode
        return newNode
    curr = head
    while True:
        nextNode = curr.next
        if curr.val <= val and val<=nextNode.val:
            break
        if curr.val>nextNode.val:
            if val>=curr.val or val<=nextNode.val:
                break
        curr = curr.next
        if curr==head: #avoid loop for same values
            break
    newNode.next = curr.next
    curr.next = newNode
    return head

def printList(head):
    temp = head
    while True:
        print(temp.val,"--->", end='')
        temp = temp.next
        if temp==head:
            break

head = insertToList(head, 5)
printList(head)

'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getClosestVal(root, target):
    if not root:
        return None
    closestDistance = sys.maxsize
    curr = root
    closest = root.val
    while curr:
        if abs(target-curr.val)<closestDistance:
            closestDistance = abs(target-curr.val)
            closest = curr.val
        if curr.val < target:
            curr=curr.right
        else:
            curr = curr.left
    return closest
    
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

target = 3.714286
print(f"Closes to {target} is {getClosestVal(root, target)}")
target = 4.4
print(f"Closes to {target} is {getClosestVal(root, target)}")

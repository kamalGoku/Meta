'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes. 
 (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the 
path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree 
if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getLeftNodes(root):
    st = []
    curr = root
    while curr:
        if not isLeaf(curr):
            st.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    return st

def getRightNodes(root):
    st = []
    curr = root
    while curr:
        if not isLeaf(curr):
            st.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    return st[::-1]

def isLeaf(root):
    return (root.left==None and root.right==None)

def getLeaves(root, ):
    st = []
    leaves = []
    curr = root
    while True:
        if curr:
            st.append(curr)
            curr = curr.left
        elif st:
            curr =st.pop()
            if isLeaf(curr):
                leaves.append(curr.val)
            curr = curr.right
        else:
            break

    return leaves

def getBoundary(root): #TC: O(H) + O(N) + O(H)
    if not root:
        return []
    if isLeaf(root):
        return [root.val]
    left = getLeftNodes(root.left)
    leaves = getLeaves(root)
    right = getRightNodes(root.right)

    return [root.val] + left + leaves + right

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(8)

root.right.left = Node(6)
root.right.left.left = Node(9)
root.right.left.right = Node(10)

print("Boundary of given BT = ", getBoundary(root))

root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(4)
print("Boundary of given BT = ", getBoundary(root))

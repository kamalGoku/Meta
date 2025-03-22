'''
VERTICAL ORDER of Binary Tree

Edge case:
- Node is NULL
- Left skewed, right skewed

BFS is more efficient as it avoid recursion

'''
from collections import defaultdict
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printTree(root):
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

def dfs(root, offset, nodeMap):
    nodeMap[offset].append(root.val)
    if root.left: dfs(root.left, offset-1, nodeMap)
    if root.right: dfs(root.right, offset+1, nodeMap)

def printVerticalOrderDFS(root):
    if not root:
        return []
    nodeMap = defaultdict(list)
    dfs(root, 0, nodeMap)
    return [val for key, val in sorted(nodeMap.items())] #O(N log N)

def printVerticalOrderBFS(root):
    if not root:
        return []
    nodeMap = defaultdict(list) #TC: O(N)
    q = deque() #TC: O(N)
    q.append((root, 0))
    while q:
        node, offset = q.popleft()
        nodeMap[offset].append(node.val)
        if node.left:
            q.append((node.left, offset-1))
        if node.right:
            q.append((node.right, offset+1))
    return [val for key, val in sorted(nodeMap.items())] #TC: O(N log N)
'''
Input: [3,9,20,null,null,15,7]
           3
        9     20
            15  7
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
'''

'''
#Input: [3,9,8,4,0,1,7]
          3
        9    8
      4  0  1  7
'''
root = Node(3)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(7)
#printTree(root)
#print(printVerticalOrderDFS(root))
print(printVerticalOrderBFS(root))

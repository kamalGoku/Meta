'''
Diameter of N-Ary Tree

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree.
This path may or may not pass through the root.'

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
                        1
                   /  /   \   \ 
                2   3      4   5
                  /  \    /   /  \
                  6   7  8    9  10
                     /   /    /
                    11  12   13
                    /
                   14
'''
from collections import defaultdict
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
root = Node(1)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
root.children += [Node(2), node3, node4, node5]
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node3.children += [Node(6), node7]
node4.children += [node8]
node5.children += [node9, Node(10)]
node11 = Node(11)
node7.children += [node11]
node8.children += [Node(12)]
node9.children += [Node(13)]
node11.children += [Node(14)]

def traverse(root, tree):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        tree.append(curr.val)
        for ch in curr.children:
            q.append(ch)

'''
TC: O(N)
SC: O(H)
'''
def diameterOfNAryTree(root):
    diameter = 0
    def dfs(root):
        nonlocal diameter
        if not root:
            return 0
        firstHeight = 0
        secondHeight = 0
        for ch in root.children:
            currHeight = dfs(ch)
            if currHeight > firstHeight:
                firstHeight = currHeight
            elif currHeight > secondHeight:
                secondHeight = currHeight
        #print(f"For node {root.val}, first {firstHeight}, second = {secondHeight}")
        diameter = max(diameter, firstHeight+secondHeight)
        return max(firstHeight, secondHeight)+1
    dfs(root)
    return diameter

tree = []
traverse(root, tree)
print("Given N-Ary Tree: ", tree)
print("Diameter of N-Ary Tree = ", diameterOfNAryTree(root))


    

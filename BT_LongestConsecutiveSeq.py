'''
298. Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along
the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
   1
    \
     3
    / \
   2   4
        \
         5
'''
root = Node(1)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
root.right.right.right = Node(5)

'''
   2
    \
     3
    /
   2
  /
 1
'''
root1 = Node(2)
root1.right = Node(3)
root1.right.left = Node(2)
root1.right.left.left = Node(1)

def longestConsecutivePath(root): #TC: O(N), SC: O(H)
    if not root:
        return 0
    res = 1
    def dfs(root, currVal, seq):
        nonlocal res
        if not root:
            return
        currSeq = 1
        if root.val == currVal+1:
            currSeq = seq+1
            res = max(res, currSeq)
        dfs(root.left, root.val, currSeq)
        dfs(root.right, root.val, currSeq)
    dfs(root, root.val, 1)
    return res

def longestConsecutivePathIterative(root):#TC: O(N), SC: O(H)
    if not root:
        return 0
    res = 1
    st = []
    st.append((root, -1, 1))
    while st:
        curr, prev, seq = st.pop()
        currSeq = 1
        if prev+1==curr.val:
            currSeq = seq+1
            res = max(res, currSeq)
        if curr.left:
            st.append((curr.left, curr.val, currSeq))
        if curr.right:
            st.append((curr.right, curr.val, currSeq))
    return res

print(longestConsecutivePath(root))
print(longestConsecutivePath(root1))

print(longestConsecutivePathIterative(root))
print(longestConsecutivePathIterative(root1))

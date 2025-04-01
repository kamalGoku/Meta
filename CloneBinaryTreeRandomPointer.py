'''
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.


'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.random = None

'''
root = [[1,null],null,[4,3],[7,0]]
             1
             |      4
             ----7
'''


def cloneBinaryTree(root):
    oldToNew = {None:None}

    def copyNodes(root):
        if not root:
            return None
        oldToNew[root] = Node(root.val)
        if root.left:
            oldToNew[root].left = copyNodes(root.left)
        if root.right:
            oldToNew[root].right = copyNodes(root.right)
        return oldToNew[root]

    def updateRandom(root):
        if not root:
            return
        oldToNew[root].random = oldToNew[root.random]
        updateRandom(root.left)
        updateRandom(root.right)

    newRoot = copyNodes(root)
    updateRandom(root)
    return oldToNew[root]


def cloneBinaryTreeSinglePass(root):
    oldToNew = {None:None}

    def copyNodes(root):
        if not root:
            return None
        if root in oldToNew:
            return oldToNew[root] 
        oldToNew[root] = Node(root.val)
        oldToNew[root].random = copyNodes(root.random)
        if root.left:
            oldToNew[root].left = copyNodes(root.left)
        if root.right:
            oldToNew[root].right = copyNodes(root.right)
        return oldToNew[root]

def printNodes(root, nodes):
    if not root:
        nodes.append("null")
        return
    nodes.append([root.val, root.random.val if root.random else "null"])
    printNodes(root.left, nodes)
    printNodes(root.right, nodes)

root = Node(1)
root.right = Node(4)
root.right.left = Node(7)
root.right.left.random = root
newRoot = cloneBinaryTree(root) #2 pass approach
nodesToPrint = []
printNodes(newRoot, nodesToPrint)
print("Copy Nodes with 2 pass : ", nodesToPrint)
newRoot1 = cloneBinaryTreeSinglePass(root)
nodesToPrint = []
printNodes(newRoot, nodesToPrint)
print("Copy Nodes with SINGLE pass : ", nodesToPrint)

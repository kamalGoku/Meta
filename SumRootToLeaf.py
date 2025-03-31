'''
Find Sum Root-To-Leaf  with node values greater than 9

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findDigits(val):
    digits = 0
    while val:
        digits+=1
        val = val//10
    return digits

def dfs(root, currSum):
    if not root:
        return 0
    if not root.left and not root.right:
        return currSum*(10**findDigits(root.val))+root.val
    print(findDigits(root.val))
    currVal = currSum*(10**findDigits(root.val))+root.val
    return dfs(root.left, currVal)+ \
           dfs(root.right, currVal)

def getSumIterative(root):
    st = []
    st.append((root, 0))
    totalSum = 0
    while st:
        curr, currSum = st.pop()
        if not curr.left and not curr.right:
            totalSum += currSum*(10**findDigits(curr.val))+curr.val
            continue
        currVal = currSum*(10**findDigits(curr.val))+curr.val
        if curr.left:
            st.append((curr.left, currVal))
        if curr.right:
            st.append((curr.right, currVal))
    return totalSum

def getRootToLeafSum(root):
    return dfs(root, 0)
'''
         3
    79       2
        111
'''
root = Node(3)
root.left = Node(79)
root.right = Node(2)
root.left.right = Node(111)
print("Sum Root to Leaf:", getRootToLeafSum(root))
print("Sum Root to Leaf:", getSumIterative(root))

'''
Variant: is the nodes have negative value
is the path has odd number of negative signs then the number is negative
'''
print("*******Sum with Negative Values************")
def getNegSumIterative(root):
    st = []
    st.append((root, 0, 0)) #node, sum, negatives
    totalSum = 0
    while st:
        curr, currSum, negatives = st.pop()

        if curr.val<0:
            negatives+=1

        currVal = (currSum*10)+abs(curr.val)

        if not curr.left and not curr.right:
            totalSum += -currVal if negatives%2 else currVal
            continue

        if curr.left:
            st.append((curr.left, currVal, negatives))
        if curr.right:
            st.append((curr.right, currVal, negatives))
            
    return totalSum
'''
            -1
        -2       4
    -9        -5
    -129+145 = 16
'''
root = Node(-1)
root.left = Node(-2)
root.right = Node(4)
root.left.left = Node(-9)
root.right.left = Node(-5)
print("Sum Root to Leaf:", getNegSumIterative(root))

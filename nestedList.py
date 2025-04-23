'''
339. Nested List Weight Sum
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
'''
from collections import deque

def depthSum(nestList, depth): #TC: O(N), SC: O(H)
    sumVal = 0
    for currVal in nestList:
        if type(currVal)==list:
            sumVal+=depthSum(currVal, depth+1)
        else:
            sumVal+=(currVal*depth)
    return sumVal

def depthSumIterative(nestList): #TC: O(N), SC: O(H)
    st = []
    sumVal = 0
    st.append((nestList,1))
    while st:
        currList, depth = st.pop()
        for item in currList:
            if type(item)==list:
                st.append((item, depth+1))
            else:
                sumVal+=(item*depth)
    return sumVal
inputList = [[1,1],2,[1,1]]
print(depthSum(inputList, 1))
inputList = [1,[4,[6]]]
print(depthSum(inputList, 1))

inputList = [[1,1],2,[1,1]]
print(depthSumIterative(inputList))
inputList = [1,[4,[6]]]
print(depthSumIterative(inputList))

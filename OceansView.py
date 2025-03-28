'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Example 2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Example 3:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Example 4:
Input: heights = [2,2,2,2]
Output: [3]
'''
#TC: O(N)
#SC : O(N)
def findBuildings(heights):
    if len(heights)==1:
        return [0]
    rightMax = heights[-1]
    res = []
    res.append(len(heights)-1)
    for idx in range(len(heights)-2, -1, -1):
        if heights[idx]>rightMax:
            res.append(idx)
            rightMax = idx
    return res[::-1]

#TC: O(N)
#SC : O(N)
def findLeftandRightBuildings(heights):
    if len(heights)==1:
        return [0]
    l=0
    r=len(heights)-1
    left = [l]
    right = [r]
    leftMax = heights[l]
    rightMax = heights[r]
    while l<r:
        if leftMax<rightMax:
            l+=1
            if heights[l]>leftMax and l<r:
                left.append(l)
                leftMax = heights[l]
        else:
            r-=1
            if heights[r]>rightMax and l<r:
                right.append(r)
                rightMax = heights[r]
    
    return left + right[::-1]
        

heightsArray = [[4,2,3,1],
                [4,3,2,1],
                [1,3,2,4],
                [2,2,2,2]]

for heights in heightsArray:
    print(findBuildings(heights))

print("Both left and right side ocean..")
for heights in heightsArray:
    print(findLeftandRightBuildings(heights))

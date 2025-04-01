'''
Given an array of pairs dominoes and an integer target,
return number of unique domino pairs [a1,a2] and [b1,b2] where a1+b1 = target and a2+b2=target 

Note:Number are limitted to 0-9
 

Example 1:
Input: nums = [[3,4],[1,9],[3,4],[2,1],[9,1],[9,1],[7,6],[1,9]], target = 10
Output: 6

Example 2:
Input: nums = [[0,0][0,0],[0,0],[0,0],[0,0]], target = 0
Output: 10
'''
def getDominoCount(nums, target) -> int:
    dMap = {}
    count = 0
    for a,b in nums:
        compliment = (target-a, target-b)
        if compliment in dMap:
            count += dMap[compliment]
        if (a,b) in dMap:
            dMap[(a,b)] += 1
        else:
            dMap[(a,b)] = 1
    return count

def getDominoCountWithInt(nums, target) -> int:
    dMap = {}
    count = 0
    for a,b in nums:
        complimentInt = (target-a)*10 + (target-b)
        if complimentInt in dMap:
            count += dMap[complimentInt]
        intKey = (a*10) + b
        if intKey in dMap:
            dMap[intKey] += 1
        else:
            dMap[intKey] = 1
    return count

#nums = [[3,4],[1,9],[3,4],[2,1],[9,1],[9,1],[7,6],[1,9]]
#target = 10

nums = [[0,0],[0,0],[0,0],[0,0],[0,0]]
target = 0
print("Domino Count = ", getDominoCountWithInt(nums, target))


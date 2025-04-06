'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''


def missingRanges(nums, lower, upper):
    res = []
    nums.append(upper+1)
    currLower = lower
    for i in range(len(nums)):
        diff = nums[i]-currLower
        if diff==1:
            res.append(str(nums[i]-1))
        elif diff>1:
            res.append(str(currLower)+'->'+str(nums[i]-1))
        currLower = nums[i]+1
            
    return res


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(missingRanges(nums, lower, upper))
nums = [2, 3, 50, 75]
lower = 1
upper = 75
print(missingRanges(nums, lower, upper))
#TC: O(N)
#SC: O(N)

'''
Count of unique elements
Given an array of integers nums sorted in non-decreasing order, find the count of unique elements in the array

You must write an algorithm with O(k log n) runtime complexity, where k in number of unique elements

Example 1:
Input: nums = [5,7,7,8,8,10]
Output: 4

Example 2:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 9
'''

def upperBound(nums, target) -> int:
    start = 0
    end = len(nums)-1
    last = 0
    while start<=end:
        mid = (start+end)//2
        if nums[mid]>target:
            end = mid-1
        else:
            last = mid
            start = mid+1
    return last

def findUniqueNumCount(nums) -> int:
    position = 0
    count  = 0
    while position<len(nums):
        target = nums[position]
        position = upperBound(nums, target)
        count += 1
        position+=1
    return count

#nums = [5,7,7,8,8,10]
#nums = [1,2,3,4,5,6,7,8,9]
nums = []
print("Unique elements in array = ", findUniqueNumCount(nums))

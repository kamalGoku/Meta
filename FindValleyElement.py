'''
FIND VALLEY ELEMENT

You may imagine that nums[-1] = nums[n] = +∞.
In other words, an element is always considered to be strictly less than a neighbor that is outside the array.

Example 1:
Input: nums = [1,2,3,1]
Output: 0

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 2
'''
def getValleyElementIdx(nums) -> int:
    n = len(nums)
    if n==1:
        return 0
    if nums[0]<nums[1]:
        return 0
    if nums[n-1]<nums[n-2]:
        return n-1
    start = 1
    end = n-2
    while start<=end:
        mid = (start+end)//2
        if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
            return mid
        elif nums[mid]<nums[mid+1]:#increasing
            end = mid-1
        else:
            start = mid+1
    return -1

#nums = [2,1,3,5,6]
#nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]
nums = [10, 5, 7, 3, 1, 4, 6]
print("Valey Element Index = ", getValleyElementIdx(nums))

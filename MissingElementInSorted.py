'''
1060. Missing Element in Sorted Array
Description
Given an integer array nums which is sorted in ascending order and
all of its elements are unique and given also an integer k,
return the kth missing number starting from the leftmost number of the array.

Example 1:
Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.

Example 2:
Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Constraints:
1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 108
'''

def getkthMissingNumber(nums, k):
    '''
    [4,7,9,10]
     0 1 2  3
    
    missing = nums[end]-nums[0]-end
    ans = nums[end] + k-missing
    ans = nums[end] + k - nums[end]+nums[0]+end
    ans = k+end+nums[0]

    4+2-1
    5
    '''
    start = 0
    end = len(nums)-1
    while start<=end:
        mid = (start+end)//2
        missing = nums[mid]-nums[0]-mid
        if missing<k:
            start = mid+1
        else:
            end = mid-1
        
    return k+end+nums[0]

nums = [4,7,9,10]
k = 1
print("1st Missing number : ", getkthMissingNumber(nums, k))
nums = [4,7,9,10]
k = 3
print("3rd Missing number : ", getkthMissingNumber(nums, k))
nums = [1,2,4]
k = 3
print("3rd Missing number : ", getkthMissingNumber(nums, k))

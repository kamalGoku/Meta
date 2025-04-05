'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector
efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
'''

#BF: multiply each value and sum it

class SparseVector:
    def __init__(self, v):
        self.nums = v
        self.numIndex = []
        for i in range(len(self.nums)):
            if self.nums[i]!=0:
                self.numIndex.append((i, self.nums[i]))
    
    '''
    def dotProduct(self, v): #TC: O(N+M)
        res = 0
        i = 0
        j = 0
        while i<len(self.numIndex) and j<len(v.numIndex):
            if self.numIndex[i][0] == v.numIndex[j][0]:
                res += self.numIndex[i][1]*v.numIndex[j][1]
                i+=1
                j+=1
            elif self.numIndex[i][0]<v.numIndex[j][0]:
                i+=1
            else:
                j+=1
        return res'
    '''

    def binarySearch(self,target, val, nums):
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid][0]==target:
                return nums[mid][1]
            elif nums[mid][0]<target:
                start=mid+1
            else:
                end = mid-1
        return 0

    def dotProduct(self, v): #TC: O(N logM) , N<<M
        res = 0
        if len(self.numIndex) < len(v.numIndex):
            for idx, val in self.numIndex:
                res += val*self.binarySearch(idx, val, v.numIndex)
        else:
            for idx, val in v.numIndex:
                res += val*self.binarySearch(idx, val, self.numIndex)
        return res

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))

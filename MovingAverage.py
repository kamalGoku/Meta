'''
MOVING AVERAGEin DATA STREAM

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
from collections import deque

class MovingAverage:
    def __init__(self, window):
        self.window = window
        self.totalSum = 0
        self.q = deque()
    
    def next(self, val):
        self.q.append(val)
        self.totalSum+=val
        if len(self.q)>self.window:
            front = self.q.popleft()
            self.totalSum -= front
        return (self.totalSum)/len(self.q)


m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))

#TC: O(1) for next and SC is O(K) where K is window size

'''
Variant: Given an array
'''

nums = [5,2,8,14,3]
size = 3
res = []
left = 0
totalSum = 0
for right in range(len(nums)):
    totalSum += nums[right]
    if right-left==size:
        totalSum-=nums[left]
        left+=1
    if right>=size-1:
        res.append(totalSum/size)
print(res)

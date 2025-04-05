'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

#using line sweep algo
#TC: O(maxVal*N)
#using minHeap, TC: O(N logN) , efficient if N is large
import heapq
meetings = [[1,5],[9,11],[3,10],[2,7]]
def getMinMeetingRooms(meetings):
    maxVal = max(meetings)[1]
    mark = [0 for _ in range(maxVal+1)]
    for start,end in meetings:
        mark[start]+=1
        mark[end]-=1

    minRooms = 0
    currRooms = 0
    for i in range(maxVal+1):
        currRooms += mark[i]
        minRooms = max(minRooms, currRooms)
    return minRooms

def getMinMeetingRoomsWithHeap(meetings):
    pq = []
    meetings.sort()
    for start, end in meetings:
        if pq and pq[0]<=start:
            heapq.heappop(pq)
        heapq.heappush(pq,end)
    return len(pq)

print("With line sweep: ", getMinMeetingRooms(meetings))
print("With min heap:", getMinMeetingRooms(meetings))

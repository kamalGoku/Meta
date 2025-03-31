'''
Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B.
Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution

A naive method can combine the two list, and sort and apply merge interval in the leetcode, but is not efficient enough.

For example,
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]

output [1,6], [8, 20]

TC: O(A+B)
SC: O(A+B)
'''

#A = [[3,11], [14,15], [18,22], [23,24], [25,26]]
#B = [[2,11], [13,22], [23,24], [25,26]]

A = [[1,5], [10,14], [16,18]]
B = [[2,6], [8,10], [11,20]]

def merge(currInterval, res):
    if not res or currInterval[0]>res[-1][1]:
        res.append(currInterval)
    else:
        res[-1][1] = max(res[-1][1], currInterval[1])
    
def mergeSortedIntervals(A, B):
    p = 0
    q = 0
    res = []
    while p<len(A) and q<len(B):
        if A[p][0] < B[q][0]:
            currInterval = A[p]
            p+=1
        else:
            currInterval = B[q]
            q+=1

        merge(currInterval, res)
    
    while p<len(A):
        merge(A[p], res)
        p+=1

    while q<len(B):
        merge(B[q], res)
        q+=1
    return res
print(mergeSortedIntervals(A,B))

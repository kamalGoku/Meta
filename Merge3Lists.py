'''
MERGE 3 SORTED LISTS

Given listA, listB and listC. each sorted in non-decreasing order
merge 3 lists to one sorted list and return it

TC: O(N)
SC: O(N)

If more than 3 lists then heap is the best way to merge

'''
import sys

def mergeLists(listA, listB, listC):
    res = []
    i=0
    j=0
    k=0
    while i<len(listA) or j<len(listB) or k<len(listC):
        aVal = listA[i] if i<len(listA) else sys.maxsize
        bVal = listB[j] if j<len(listB) else sys.maxsize
        cVal = listC[k] if k<len(listC) else sys.maxsize
        minVal = min(aVal, bVal, cVal)
        res.append(minVal)
        if minVal==aVal:
            i+=1
        elif minVal==bVal:
            j+=1
        else:
            k+=1
    return res


listA = [1,1,2,2,3,4]
listB = [3,3,4,5,6]
listC = [2,3,7,8,9,10]
print(mergeLists(listA, listB, listC))

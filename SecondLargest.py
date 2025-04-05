'''
Build Second largest number
'''
def getSecondLargest(num):
    freq = [0 for _ in range(10)]
    res = []
    for digit in num:
        freq[digit]+=1
    
    for i in range(9,-1,-1):
        for _ in range(freq[i]):
            res.append(i)
    
    for i in range(len(res)-1, -1, -1):        
        if res[i]!=res[i-1]:
            res[i],res[i-1]=res[i-1],res[i]
            return res
    
    return []

#num = [2,7,3,6]
#num = [1,0,0,8,9]
#num = [9,9,9]
num = [1, 0, 0, 8, 9]
#num = [0,0,1]
print(getSecondLargest(num))
#TC: 3xO(N) ~ O(N)
#SC: O(10) ~ O(1)

'''
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

Remove all duplicates

 

Example 1:

Input: s = "abbbacxdd"
Output: "cx"


Input: s = "azxxzy"
Output: "ay"

TC: O(N)
SC: O(N)
'''
def removeDuplicates(s):
    res = []
    for c in s:
        if res and res[-1][0]==c:
            res[-1][1]+=1
        else:
            if res and res[-1][1]>1:
                res.pop()

            if res and res[-1][0]==c: #same as prev
                res[-1][1]+=1
            else:
                res.append([c,1])
    
    if res and res[-1][1]>1:
        res.pop()
    
    return "".join(c*freq for c,freq in res)

print(removeDuplicates("abbbacxdd"))
print(removeDuplicates("azxxzy"))

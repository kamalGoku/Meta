'''
249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

from collections import defaultdict

def getAscii(c):
    return ord(c)-ord('a')

def groupShiftedStrings(strings):
    diffMap = defaultdict(list)
    for s in strings:
        diffs = []
        for i in range(1, len(s)):
            diffs.append((getAscii(s[i-1])-getAscii(s[i]))%26)
        diffMap[tuple(diffs)].append(s)

    res = []
    for _, strs in diffMap.items():
        res.append(strs)

    return res
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

print(groupShiftedStrings(strings)) 
#TC: O(N*M), N-no of words, M-avg len of each word
#SC: O(N*M)

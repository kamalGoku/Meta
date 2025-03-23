'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
'''

def isValidAbbr(word, abbr):
    wPtr = 0
    aPtr = 0
    while wPtr<len(word) and aPtr<len(abbr):
        if abbr[aPtr].isdigit():
            if abbr[aPtr]=='0':
                return False
            steps = ''
            while aPtr<len(abbr) and abbr[aPtr].isdigit():
                steps+=abbr[aPtr]
                aPtr+=1
            steps = int(steps)
            if wPtr+steps>len(word):
                return False
            wPtr+=steps
        else:
            if word[wPtr]!=abbr[aPtr]:
                return False
            wPtr+=1
            aPtr+=1

    if wPtr==len(word) and aPtr==len(abbr) :
        return True
    return False

words = ["internationalization", "apple", "apple", "appleeeeeeeeeeeeeeeeeeeeeee", "appleeeeeeeeeeeeeeeeeeee", "substitution"]
abbrs = ["i12iz4n", "apple", "a2e", "a22e",  "a22e", "s0ubstitution"]
for i in range(len(words)):
    print(f"For {words[i]}: ", isValidAbbr(words[i], abbrs[i]))

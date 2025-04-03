'''
Add Decimal strings

Example 1:
Input: num1 = "11.11" , num2 = "123.5"
Output: "134.61"

Example 2:
Input: num1 = "9." , num2 = "9.4"
Output: "18.4"

Example 3:
Input: num1 = ".15" , num2 = "612"
Output: "612.15"

'''

def addStrings(num1, num2):
    def splitNum(num):
        if '.' in num:
            int, dec = num.split('.')
        else:
            int, dec = num, ''
        return int, dec
    
    int1, dec1 = splitNum(num1)
    int2, dec2 = splitNum(num2)

    def addNums(a, b, carry):
        l1 = len(a)-1
        l2 = len(b)-1
        res = []
        while l1>=0 or l2>=0 or carry:
            d1 = ord(a[l1])-ord('0') if l1>=0 else 0
            d2 = ord(b[l2])-ord('0') if l2>=0 else 0
            currSum = d1+d2+carry
            carry = currSum//10
            currSum = currSum%10
            res.append(chr(currSum+ord('0')))
            l1-=1
            l2-=1
        return ''.join(reversed(res))

    carry = 0
    maxDecLen = max(len(dec1), len(dec2))
    dec1 += '0'*(maxDecLen-len(dec1))
    dec2 += '0'*(maxDecLen-len(dec2))
    dec = addNums(dec1, dec2, carry)
    if len(dec)>maxDecLen:
        carry = ord(dec[:1])-ord('0')
        dec = dec[1:]
    intPart = addNums(int1, int2, carry)
    if dec:
        return intPart + '.' + dec
    else:
        return intPart

input = [["11.11", "123.5"], [".15", "612"], ["9.","9.4"], ["1", "34"], ["9.99", "9.99"], ["1.50", "2.50"]]
for num1, num2 in input:
    print(addStrings(num1, num2))

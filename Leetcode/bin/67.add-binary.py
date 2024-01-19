#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (53.04%)
# Likes:    9088
# Dislikes: 922
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        
        aLen = len(a)
        bLen = len(b)
        
        while aLen != bLen:
            if aLen>bLen: 
                b = "0"+b
                bLen += 1
            else : 
                a = "0"+a
                aLen += 1
        
        for i in range(-1,-aLen-1,-1):
            sum = int(a[i]) + int(b[i]) + carry
            if sum == 3:
                ans = "1" + ans
                carry = 1
            elif sum == 2:
                ans = "0" + ans
                carry = 1
            elif sum == 1:
                ans = "1" + ans
                carry = 0
            else:
                ans = "0" + ans
                carry = 0
        if carry == 1: ans = "1" + ans
        return ans
# @lc code=end


#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (53.91%)
# Likes:    5199
# Dislikes: 347
# Total Accepted:    593.2K
# Total Submissions: 1.1M
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
# 
# 
# Example 1:
# 
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# 
# 
#
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sSet = set()

        for char in s:
            if char not in sSet:
                sSet.add(char)
            else:
                sSet.remove(char)
        
        unique = len(sSet)-1 if len(sSet) != 0 else 0
        return len(s) - unique
# @lc code=end


#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.34%)
# Likes:    38545
# Dislikes: 1786
# Total Accepted:    5.4M
# Total Submissions: 15.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        ans = 0
        sMap = {}
        left = 0
        length = len(s)

        for right in range(length):
            if s[right] not in sMap or sMap[s[right]] < left:
                sMap[s[right]] = right
                ans = max(ans,right-left+1)
            else:
                left = sMap[s[right]] + 1
                sMap[s[right]] = right
        return ans
        # ans = 0
        # lastLen = 0
        # tempSet = set()
        # start = 0
        # i = 0
        # while i < len(s):
        #     tempSet.add(s[i])
        #     if len(tempSet) <= lastLen:
        #         lastLen = 1
        #         start += 1
        #         i = start
        #         tempSet.clear()
        #         tempSet.add(s[start])
        #     else:  
        #         lastLen = len(tempSet)
        #         ans = max(lastLen,ans)
        #     i += 1
        # return ans
# @lc code=end


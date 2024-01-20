#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (61.24%)
# Likes:    11428
# Dislikes: 1268
# Total Accepted:    3.6M
# Total Submissions: 5.9M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
# 
# 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for num in nums:
            numMap[num] = numMap[num] + 1 if numMap.get(num) else 1
            if numMap[num] > 1: return True
        return False
# @lc code=end


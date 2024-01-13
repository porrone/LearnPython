#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (56.97%)
# Likes:    11335
# Dislikes: 233
# Total Accepted:    2.2M
# Total Submissions: 3.8M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        if nums[0] == target: return 0
        high = len(nums)
        index = int(high/2)
        low = 0
        while not high-low <= 1:
            if nums[index] == target: return index
            if nums[index] < target:
                low = index
                index = int(low + (high-low)/2)
            else:
                high = index
                index = int(low + (high-low)/2)
        return -1
# @lc code=end


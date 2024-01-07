#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {};
        for i in range(len(nums)):
            inverse = target - nums[i]
            if inverse in numMap:
                return [i,numMap[inverse]]
            numMap[nums[i]] = i
        return []
        
# @lc code=end

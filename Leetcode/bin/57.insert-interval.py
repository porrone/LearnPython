#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (39.75%)
# Likes:    9424
# Dislikes: 697
# Total Accepted:    920.2K
# Total Submissions: 2.3M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
# 
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals)-1):
            # fully encased by another list entity
            if newInterval[0] > intervals[i][0] and newInterval[1] < intervals[i][1]: return intervals
            # fully outside of another list entity
            elif newInterval[0] > intervals[i][1] and newInterval[1] < intervals[i+1][0]:
                intervals.insert(i+1,newInterval)
                return intervals
            # overlapping top end of one interval
            elif newInterval[0] <= intervals[i][0] and newInterval[1] < intervals[i+1][0] and newInterval[1] > intervals[i][1]:
                intervals[i][1] = newInterval[1]
                return intervals
            # overlapping bottom end of next interval
            elif newInterval[0] > intervals[i][1] and newInterval[1] >= intervals[i][0] and newInterval[1] < intervals[i][1]:
                intervals.insert(i+1,newInterval)
                return intervals
            # overlapping top and bottom end of one interval
            elif False:
                pass
            # bridging two or more intervals
            elif False:
                pass
        return intervals
# @lc code=end


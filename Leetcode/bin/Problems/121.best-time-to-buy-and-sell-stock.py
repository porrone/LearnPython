#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for price in prices[1:]:
            profit = max(profit,price - minPrice)
            minPrice = min(minPrice,price)
        return profit
# @lc code=end


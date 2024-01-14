#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (63.44%)
# Likes:    8081
# Dislikes: 813
# Total Accepted:    837.6K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
# 
# You are also given three integers sr, sc, and color. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
# 
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
# 
# Return the modified image after performing the flood fill.
# 
# 
# Example 1:
# 
# 
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
# 
# 
# Example 2:
# 
# 
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made
# to the image.
# 
# 
# 
# Constraints:
# 
# 
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
# 
# 
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, first: bool = True, initialColor: int = 0) -> List[List[int]]:
        if first: 
            initialColor = image[sr][sc]
            first = False
        if initialColor == color: return image

        columns = len(image[0])-1
        rows = len(image)-1
        if sr < 0 or sc < 0 or sr > rows or sc > columns: return image

        if image[sr][sc] == initialColor: image[sr][sc] = color
        if sr + 1 <= rows and image[sr+1][sc] == initialColor: self.floodFill(image,sr+1,sc,color,first,initialColor)
        if sr - 1 >= 0 and image[sr-1][sc] == initialColor: self.floodFill(image,sr-1,sc,color,first,initialColor)
        if sc + 1 <= columns and image[sr][sc+1] == initialColor: self.floodFill(image,sr,sc+1,color,first,initialColor)
        if sc - 1 >= 0 and image[sr][sc-1] == initialColor: self.floodFill(image,sr,sc-1,color,first,initialColor)

        return image
# @lc code=end


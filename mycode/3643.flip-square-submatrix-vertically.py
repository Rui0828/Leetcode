#
# @lc app=leetcode id=3643 lang=python3
#
# [3643] Flip Square Submatrix Vertically
#

# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        for i in range(k // 2):
            grid[x+i][y:y+k], grid[x+k-1-i][y:y+k] = grid[x+k-1-i][y:y+k], grid[x+i][y:y+k]
        return grid
# @lc code=end


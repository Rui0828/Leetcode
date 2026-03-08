#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trans = list(zip(*grid))
        cnt = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i] == list(trans[j]):
                    cnt += 1
        return cnt
# @lc code=end


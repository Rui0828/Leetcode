#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#

# @lc code=start
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j>0:
                    grid[i][j] += grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
                elif i>0:
                    grid[i][j] += grid[i-1][j]
                elif j>0:
                    grid[i][j] += grid[i][j-1]
                
                if grid[i][j] <= k:
                    cnt += 1
        

        return cnt
        
# @lc code=end


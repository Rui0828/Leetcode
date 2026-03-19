#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#

# @lc code=start
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c = grid[i][j]
                grid[i][j] = [0,0]
                if i>0 and j>0:
                    grid[i][j][0] = grid[i-1][j][0]+grid[i][j-1][0]-grid[i-1][j-1][0]
                    grid[i][j][1] = grid[i-1][j][1]+grid[i][j-1][1]-grid[i-1][j-1][1]
                elif i>0:
                    grid[i][j][0] = grid[i-1][j][0]
                    grid[i][j][1] = grid[i-1][j][1]
                elif j>0:
                    grid[i][j][0] = grid[i][j-1][0]
                    grid[i][j][1] = grid[i][j-1][1]
                
                if c=="X":
                    grid[i][j][0]+=1
                elif c=="Y":
                    grid[i][j][1]+=1
                
                if grid[i][j][0] and grid[i][j][0] == grid[i][j][1]:
                    cnt += 1
        
        return cnt
        
# @lc code=end


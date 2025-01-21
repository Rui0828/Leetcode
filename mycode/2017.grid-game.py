#
# @lc app=leetcode id=2017 lang=python
#
# [2017] Grid Game
#

# @lc code=start
class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_grid = len(grid[0])
        
        if len_grid == 1:
            return 0
        
        suffix1 = [grid[0][-1]]
        prefix2 = [grid[1][0]]
        
        
        for i in range(1, len_grid):
            prefix2.append(grid[1][i] + prefix2[-1])
            suffix1.append(grid[0][len_grid-i-1] + suffix1[-1])
        
        suffix1.reverse()
        
        min_score = suffix1[1]
        
        for i in range(1, len_grid-1):
            max2 = max(prefix2[i-1], suffix1[i+1])
            if max2 < min_score:
                min_score = max2
        
        min_score = min(min_score, prefix2[len_grid-2])
        
        return min_score
# @lc code=end

print(Solution().gridGame([[2,5,4],[1,5,1]])) # 4
print(Solution().gridGame([[3,3,1],[8,5,2]])) # 4
print(Solution().gridGame([[1,3,1,15],[1,3,3,1]])) # 7
print(Solution().gridGame([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]])) # 63
print(Solution().gridGame([[1],[2]])) # 0

